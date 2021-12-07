# Copyright (c) Microsoft Corporation.
# Licensed under the MIT license.

import warnings
from typing import Optional, Union

import networkx as nx
import numpy as np
from beartype import beartype

from graspologic.embed import AdjacencySpectralEmbed
from graspologic.embed.base import SvdAlgorithmType
from graspologic.preconditions import check_argument, is_real_weighted
from graspologic.utils import (
    augment_diagonal,
    is_fully_connected,
    pass_to_ranks,
    remove_loops,
)

from . import __SVD_SOLVER_TYPES  # from the module init
from ._elbow import _index_of_elbow
from .embeddings import Embeddings


@beartype
def adjacency_spectral_embedding(
    graph: Union[nx.Graph, nx.DiGraph, nx.OrderedGraph, nx.OrderedDiGraph],
    dimensions: int = 100,
    elbow_cut: Optional[int] = None,
    svd_solver_algorithm: SvdAlgorithmType = "randomized",
    svd_solver_iterations: int = 5,
    svd_seed: Optional[int] = None,
    weight_attribute: str = "weight",
) -> Embeddings:
    """
    Given a directed or undirected networkx graph (*not* multigraph), generate an
    Embeddings object.

    Adjacency spectral embeddings are extremely egocentric, implying that results are
    slanted toward the core-periphery of each node. This is in contrast to Laplacian
    spectral embeddings, which look further into the latent space when it captures
    change.

    `Adjacency Spectral Embedding Tutorial
    <https://microsoft.github.io/graspologic/tutorials/embedding/AdjacencySpectralEmbed.html>`_

    Graphs will always have their diagonal augmented. In other words, a self-loop
    will be created for each node with a weight corresponding to the weighted degree.

    Lastly, all weights will be rescaled based on their relative rank in the graph,
    which is beneficial in minimizing anomalous results if some edge weights are
    extremely atypical of the rest of the graph.

    Parameters
    ----------
    graph : Union[nx.Graph, nx.OrderedGraph, nx.DiGraph, nx.OrderedDiGraph]
        An undirected or directed graph. The graph **must**:

        - be fully numerically weighted (every edge must have a real, numeric weight
          or else it will be treated as an unweighted graph)
        - be a basic graph (meaning it should not be a multigraph; if you have a
          multigraph you must first decide how you want to handle the weights of the
          edges between two nodes, whether summed, averaged, last-wins,
          maximum-weight-only, etc)
    dimensions : int (default=100)
        Dimensions to use for the svd solver.
        For undirected graphs, if ``elbow_cut==None``, you will receive an embedding
        that has ``nodes`` rows and ``dimensions`` columns.
        For directed graphs, if ``elbow_cut==None``, you will receive an embedding that
        has ``nodes`` rows and ``2*dimensions`` columns.
        If ``elbow_cut`` is specified to be not ``None``, we will cut the embedding at
        ``elbow_cut`` elbow, but the provided ``dimensions`` will be used in the
        creation of the SVD.
    elbow_cut : Optional[int] (default=None)
        Using a process described by Zhu & Ghodsi in their paper "Automatic
        dimensionality selection from the scree plot via the use of profile likelihood",
        truncate the dimensionality of the return on the ``elbow_cut``-th elbow.
        By default this value is ``None`` but can be used to reduce the dimensionality
        of the returned tensors.
    svd_solver_algorithm : str (default="randomized")
        allowed values: {'randomized', 'full', 'truncated'}

        SVD solver to use:

            - 'randomized'
                Computes randomized svd using
                :func:`sklearn.utils.extmath.randomized_svd`
            - 'full'
                Computes full svd using :func:`scipy.linalg.svd`
                Does not support ``graph`` input of type scipy.sparse.csr_matrix
            - 'truncated'
                Computes truncated svd using :func:`scipy.sparse.linalg.svds`
    svd_solver_iterations : int (default=5)
        Number of iterations for randomized SVD solver. Not used by 'full' or
        'truncated'. The default is larger than the default in randomized_svd
        to handle sparse matrices that may have large slowly decaying spectrum.
    svd_seed : Optional[int] (default=None)
        Used to seed the PRNG used in the ``randomized`` svd solver algorithm.
    weight_attribute : str (default="weight")
        The edge dictionary key that contains the weight of the edge.

    Returns
    -------
    Embeddings

    Raises
    ------
    beartype.roar.BeartypeCallHintPepParamException if parameters do not match type hints
    ValueError if values are not within appropriate ranges or allowed values

    See Also
    --------
    graspologic.pipeline.embed.Embeddings
    graspologic.embed.AdjacencySpectralEmbed
    graspologic.embed.select_svd

    Notes
    -----
    The singular value decomposition:

    .. math:: A = U \Sigma V^T

    is used to find an orthonormal basis for a matrix, which in our case is the
    adjacency matrix of the graph. These basis vectors (in the matrices U or V) are
    ordered according to the amount of variance they explain in the original matrix.
    By selecting a subset of these basis vectors (through our choice of dimensionality
    reduction) we can find a lower dimensional space in which to represent the graph.

    References
    ----------
    .. [1] Sussman, D.L., Tang, M., Fishkind, D.E., Priebe, C.E.  "A
       Consistent Adjacency Spectral Embedding for Stochastic Blockmodel Graphs,"
       Journal of the American Statistical Association, Vol. 107(499), 2012

    .. [2] Levin, K., Roosta-Khorasani, F., Mahoney, M. W., & Priebe, C. E. (2018).
        Out-of-sample extension of graph adjacency spectral embedding. PMLR: Proceedings
        of Machine Learning Research, 80, 2975-2984.

    .. [3] Zhu, M. and Ghodsi, A. (2006). Automatic dimensionality selection from the
        scree plot via the use of profile likelihood. Computational Statistics & Data
        Analysis, 51(2), pp.918-930.

    """
    check_argument(dimensions >= 1, "dimensions must be positive")

    check_argument(elbow_cut is None or elbow_cut >= 1, "elbow_cut must be positive")

    check_argument(
        svd_solver_algorithm in __SVD_SOLVER_TYPES,
        f"svd_solver_algorithm must be one of the values in {','.join(__SVD_SOLVER_TYPES)}",
    )

    check_argument(svd_solver_iterations >= 1, "svd_solver_iterations must be positive")

    check_argument(
        svd_seed is None or 0 <= svd_seed <= 2 ** 32 - 1,
        "svd_seed must be a nonnegative, 32-bit integer",
    )

    check_argument(
        not graph.is_multigraph(),
        "Multigraphs are not supported; you must determine how to represent at most "
        "one edge between any two nodes, and handle the corresponding weights "
        "accordingly",
    )

    used_weight_attribute: Optional[str] = weight_attribute
    if not is_real_weighted(graph, weight_attribute=weight_attribute):
        warnings.warn(
            f"Graphs with edges that do not have a real numeric weight set for every "
            f"{weight_attribute} attribute on every edge are treated as an unweighted "
            f"graph - which presumes all weights are `1.0`. If this is incorrect, "
            f"please add a '{weight_attribute}' attribute to every edge with a real, "
            f"numeric value (e.g. an integer or a float) and call this function again."
        )
        used_weight_attribute = None  # this supercedes what the user said, because
        # not all of the weights are real numbers, if they exist at all
        # this weight=1.0 treatment actually happens in nx.to_scipy_sparse_matrix()

    node_labels = np.array(list(graph.nodes()))

    graph_as_csr = nx.to_scipy_sparse_matrix(
        graph, weight=used_weight_attribute, nodelist=node_labels
    )

    if not is_fully_connected(graph):
        warnings.warn("More than one connected component detected")

    graph_sans_loops = remove_loops(graph_as_csr)

    ranked_graph = pass_to_ranks(graph_sans_loops)

    augmented_graph = augment_diagonal(ranked_graph)

    embedder = AdjacencySpectralEmbed(
        n_components=dimensions,
        n_elbows=None,  # in the short term, we do our own elbow finding
        algorithm=svd_solver_algorithm,
        n_iter=svd_solver_iterations,
        svd_seed=svd_seed,
        concat=False,
        diag_aug=False,
    )
    results = embedder.fit_transform(augmented_graph)
    results_arr: np.ndarray

    if elbow_cut is None:
        if isinstance(results, tuple) or graph.is_directed():
            results_arr = np.concatenate(results, axis=1)
        else:
            results_arr = results
    else:
        column_index = _index_of_elbow(embedder.singular_values_, elbow_cut)
        if isinstance(results, tuple):
            left, right = results
            left = left[:, :column_index]
            right = right[:, :column_index]
            results_arr = np.concatenate((left, right), axis=1)
        else:
            results_arr = results[:, :column_index]

    embeddings = Embeddings(node_labels, results_arr)
    return embeddings
