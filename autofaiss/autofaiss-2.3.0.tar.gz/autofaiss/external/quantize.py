""" main file to create an index from the the begining """

import logging
from typing import Any, Tuple, Dict, Optional, Union, List
import os
import uuid
from pprint import pprint as pp
import multiprocessing
import tempfile

import faiss
import json

import fire
import fsspec
import pandas as pd

from autofaiss.readers.embeddings_iterators import read_total_nb_vectors_and_dim
from autofaiss.external.build import (
    create_index,
    estimate_memory_required_for_index_creation,
    get_estimated_construction_time_infos,
)
from autofaiss.external.optimize import get_optimal_hyperparameters, get_optimal_index_keys_v2
from autofaiss.external.scores import compute_fast_metrics, compute_medium_metrics
from autofaiss.indices.index_utils import set_search_hyperparameters
from autofaiss.utils.decorators import Timeit
from autofaiss.utils.cast import cast_memory_to_bytes, cast_bytes_to_memory_string
import numpy as np

LOGGER = logging.getLogger(__name__)


def build_index(
    embeddings: Union[str, np.ndarray],
    index_path: str = "knn.index",
    index_infos_path: str = "index_infos.json",
    ids_path: Optional[str] = None,
    save_on_disk: bool = True,
    file_format: str = "npy",
    embedding_column_name: str = "embedding",
    id_columns: Optional[List[str]] = None,
    index_key: Optional[str] = None,
    index_param: Optional[str] = None,
    max_index_query_time_ms: float = 10.0,
    max_index_memory_usage: str = "16G",
    current_memory_available: str = "32G",
    use_gpu: bool = False,
    metric_type: str = "ip",
    nb_cores: Optional[int] = None,
    make_direct_map: bool = False,
) -> Tuple[Optional[Any], Optional[Dict[str, Union[str, float, int]]]]:
    """
    Reads embeddings and creates a quantized index from them.
    The index is stored on the current machine at the given ouput path.

    Parameters
    ----------
    embeddings : Union[str, np.ndarray]
        Local path containing all preprocessed vectors and cached files.
        Files will be added if empty.
        Or directly the Numpy array of embeddings
    index_path: Optional(str)
        Destination path of the quantized model.
    index_infos_path: Optional(str)
        Destination path of the metadata file.
    ids_path: Optional(str)
        Only useful when id_columns is not None and file_format=`parquet`. T
        his will be the path (in any filesystem)
        where the mapping files Ids->vector index will be store in parquet format
    save_on_disk: bool
        Whether to save the index on disk, default to True.
    file_format: Optional(str)
        npy or parquet ; default npy
    embedding_column_name: Optional(str)
        embeddings column name for parquet ; default embedding
    id_columns: Optional(List[str])
        Can only be used when file_format=`parquet`.
        In this case these are the names of the columns containing the Ids of the vectors,
        and separate files will be generated to map these ids to indices in the KNN index ;
        default None
    index_key: Optional(str)
        Optional string to give to the index factory in order to create the index.
        If None, an index is chosen based on an heuristic.
    index_param: Optional(str)
        Optional string with hyperparameters to set to the index.
        If None, the hyper-parameters are chosen based on an heuristic.
    max_index_query_time_ms: float
        Bound on the query time for KNN search, this bound is approximative
    max_index_memory_usage: str
        Maximum size allowed for the index, this bound is strict
    current_memory_available: str
        Memory available on the machine creating the index, having more memory is a boost
        because it reduces the swipe between RAM and disk.
    use_gpu: bool
        Experimental, gpu training is faster, not tested so far
    metric_type: str
        Similarity function used for query:
            - "ip" for inner product
            - "l2" for euclidian distance
    nb_cores: Optional[int]
        Number of cores to use. Will try to guess the right number if not provided
    make_direct_map: bool
        Create a direct map allowing reconstruction of embeddings. This is only needed for IVF indices.
        Note that might increase the RAM usage (approximately 8GB for 1 billion embeddings)
    """

    current_bytes = cast_memory_to_bytes(current_memory_available)
    max_index_bytes = cast_memory_to_bytes(max_index_memory_usage)
    memory_left = current_bytes - max_index_bytes

    if memory_left < current_bytes * 0.1:
        print(
            "You do not have enough memory to build this index"
            "please increase current_memory_available or decrease max_index_memory_usage"
        )
        return None, None

    if nb_cores is None:
        nb_cores = multiprocessing.cpu_count()
    print(f"Using {nb_cores} omp threads (processes), consider increasing --nb_cores if you have more")
    faiss.omp_set_num_threads(nb_cores)

    if isinstance(embeddings, np.ndarray):
        tmp_dir_embeddings = tempfile.TemporaryDirectory()
        np.save(os.path.join(tmp_dir_embeddings.name, "emb.npy"), embeddings)
        embeddings_path = tmp_dir_embeddings.name
    else:
        embeddings_path = embeddings

    with Timeit("Launching the whole pipeline"):

        nb_vectors, vec_dim = read_total_nb_vectors_and_dim(
            embeddings_path, file_format=file_format, embedding_column_name=embedding_column_name
        )
        print(f"There are {nb_vectors} embeddings of dim {vec_dim}")

        with Timeit("Compute estimated construction time of the index", indent=1):
            print(get_estimated_construction_time_infos(nb_vectors, vec_dim, indent=2))

        with Timeit("Checking that your have enough memory available to create the index", indent=1):
            necessary_mem, index_key_used = estimate_memory_required_for_index_creation(
                nb_vectors, vec_dim, index_key, max_index_memory_usage
            )
            print(
                f"{cast_bytes_to_memory_string(necessary_mem)} of memory "
                "will be needed to build the index (more might be used if you have more)"
            )

            prefix = "(default) " if index_key is None else ""

            if necessary_mem > cast_memory_to_bytes(current_memory_available):
                r = (
                    f"The current memory available on your machine ({current_memory_available}) is not "
                    f"enough to create the {prefix}index {index_key_used} that requires "
                    f"{cast_bytes_to_memory_string(necessary_mem)} to train. "
                    "You can decrease the number of clusters of you index since the Kmeans algorithm "
                    "used for clusterisation is responsible for this high memory usage."
                    "Consider increasing the options current_memory_available or decreasing max_index_memory_usage"
                )
                print(r)
                return None, None

        if index_key is None:
            with Timeit("Selecting most promising index types given data characteristics", indent=1):
                best_index_keys = get_optimal_index_keys_v2(nb_vectors, vec_dim, max_index_memory_usage)
                if not best_index_keys:
                    return None, None
                index_key = best_index_keys[0]

        if id_columns is not None:
            print(f"Id columns provided {id_columns} - will be reading the corresponding columns")
            if ids_path is not None:
                print("\tWill be writing the Ids DataFrame in parquet format to {ids_path}")
                fs, _ = fsspec.core.url_to_fs(ids_path)
                fs.mkdirs(ids_path, exist_ok=True)
            else:
                print("\tAs ids_path=None - the Ids DataFrame will not be written and will be ignored subsequently")
                print("\tPlease provide a value ids_path for the Ids to be written")

        def write_ids_df_to_parquet(ids: pd.DataFrame, batch_id: int):
            filename = f"part-{batch_id:08d}-{uuid.uuid1()}.parquet"
            output_file = os.path.join(ids_path, filename)  # type: ignore
            with fsspec.open(output_file, "wb") as f:
                LOGGER.debug(f"Writing id DataFrame to file {output_file}")
                ids.to_parquet(f)

        with Timeit("Creating the index", indent=1):
            index = create_index(
                embeddings_path,
                index_key,
                metric_type,
                nb_vectors,
                current_memory_available,
                use_gpu=use_gpu,
                file_format=file_format,
                embedding_column_name=embedding_column_name,
                id_columns=id_columns,
                embedding_ids_df_handler=write_ids_df_to_parquet if ids_path and id_columns else None,
                make_direct_map=make_direct_map,
            )

        if index_param is None:
            with Timeit("Computing best hyperparameters", indent=1):
                index_param = get_optimal_hyperparameters(index, index_key, max_speed=max_index_query_time_ms)

        # Set search hyperparameters for the index
        set_search_hyperparameters(index, index_param, use_gpu)
        print(f"The best hyperparameters are: {index_param}")

        metric_infos: Dict[str, Union[str, float, int]] = {}
        metric_infos["index_key"] = index_key
        metric_infos["index_param"] = index_param

        with Timeit("Compute fast metrics", indent=1):
            metric_infos.update(
                compute_fast_metrics(
                    embeddings_path, index, file_format=file_format, embedding_column_name=embedding_column_name
                )
            )

        if save_on_disk:
            with Timeit("Saving the index on local disk", indent=1):
                with fsspec.open(index_path, "wb").open() as f:
                    faiss.write_index(index, faiss.PyCallbackIOWriter(f.write))
                with fsspec.open(index_infos_path, "w").open() as f:
                    json.dump(metric_infos, f)

        print("Recap:")
        pp(metric_infos)

    return index, metric_infos


def tune_index(
    index_path: Union[str, Any],
    index_key: str,
    index_param: Optional[str] = None,
    output_index_path: Optional[str] = None,
    save_on_disk: bool = True,
    max_index_query_time_ms: float = 10.0,
    use_gpu: bool = False,
) -> Tuple[Optional[Any], Optional[Dict[str, Union[str, float, int]]]]:
    """
    Set hyperparameters to the given index.

    If an index_param is given, set this hyperparameters to the index,
    otherwise perform a greedy heusistic to make the best out or the max_index_query_time_ms constraint

    Parameters
    ----------
    index_path : Union[str, Any]
        Path to .index file
        Can also be an index
    index_key: str
        String to give to the index factory in order to create the index.
    index_param: Optional(str)
        Optional string with hyperparameters to set to the index.
        If None, the hyper-parameters are chosen based on an heuristic.
    output_index_path: str
        Path to the newly created .index file
    save_on_disk: bool
        Whether to save the index on disk, default to True.
    max_index_query_time_ms: float
        Query speed constraint for the index to create.
    use_gpu: bool
        Experimental, gpu training is faster, not tested so far.

    Returns
    -------
    index
        The faiss index
    """

    if isinstance(index_path, str):
        with fsspec.open(index_path, "r").open() as f:
            index = faiss.read_index(faiss.PyCallbackIOReader(f.read))
    else:
        index = index_path

    if index_param is None:
        with Timeit("Compute best hyperparameters"):
            index_param = get_optimal_hyperparameters(index, index_key, max_speed=max_index_query_time_ms)

    with Timeit("Set search hyperparameters for the index"):
        set_search_hyperparameters(index, index_param, use_gpu)

    if save_on_disk:
        with fsspec.open(output_index_path, "wb").open() as f:
            faiss.write_index(index, faiss.PyCallbackIOWriter(f.write))

    print(f"The optimal hyperparameters are {index_param}, the index with these parameters has been saved.")

    return index


def score_index(
    index_path: Union[str, Any],
    embeddings: Union[str, np.ndarray],
    save_on_disk: bool = True,
    output_index_info_path: str = "infos.json",
    current_memory_available: str = "32G",
) -> None:
    """
    Compute metrics on a given index, use cached ground truth for fast scoring the next times.

    Parameters
    ----------
    index_path : Union[str, Any]
        Path to .index file. Or in memory index
    embeddings: Union[str, np.ndarray]
        Path containing all preprocessed vectors and cached files. Can also be an in memory array.
    save_on_disk: bool
        Whether to save on disk
    output_index_info_path : str
        Path to index infos .json
    current_memory_available: str
        Memory available on the current machine, having more memory is a boost
        because it reduces the swipe between RAM and disk.
    """
    faiss.omp_set_num_threads(multiprocessing.cpu_count())

    if isinstance(index_path, str):
        with fsspec.open(index_path, "r").open() as f:
            index = faiss.read_index(faiss.PyCallbackIOReader(f.read))
        fs, path_in_fs = fsspec.core.url_to_fs(index_path)
        index_memory = fs.size(path_in_fs)
    else:
        index = index_path
        with tempfile.NamedTemporaryFile("wb") as f:
            faiss.write_index(index, faiss.PyCallbackIOWriter(f.write))
            fs, path_in_fs = fsspec.core.url_to_fs(f.name)
            index_memory = fs.size(path_in_fs)

    if isinstance(embeddings, np.ndarray):
        tmp_dir_embeddings = tempfile.TemporaryDirectory()
        np.save(os.path.join(tmp_dir_embeddings.name, "emb.npy"), embeddings)
        embeddings_path = tmp_dir_embeddings.name
    else:
        embeddings_path = embeddings

    infos: Dict[str, Union[str, float, int]] = {}

    with Timeit("Compute fast metrics"):
        infos.update(compute_fast_metrics(embeddings_path, index))

    print("Intermediate recap:")
    pp(infos)

    current_in_bytes = cast_memory_to_bytes(current_memory_available)
    memory_left = current_in_bytes - index_memory

    if memory_left < current_in_bytes * 0.1:
        print(
            f"Not enough memory, at least {cast_bytes_to_memory_string(index_memory*1.1)}"
            "is needed, please increase current_memory_available"
        )
        return None

    with Timeit("Compute medium metrics"):
        infos.update(compute_medium_metrics(embeddings_path, index, memory_left))

    print("Performances recap:")
    pp(infos)

    if save_on_disk:
        with fsspec.open(output_index_info_path, "w").open() as f:
            json.dump(infos, f)

    return index


def main():
    """Main entry point"""
    logging.basicConfig(level=logging.INFO)

    fire.Fire({"build_index": build_index, "tune_index": tune_index, "score_index": score_index})


if __name__ == "__main__":
    main()
