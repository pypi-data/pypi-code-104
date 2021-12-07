import numpy as np
import os.path as op
import pandas as pd
import pytest
import tempfile
import torch

import afqinsight as afqi
from afqinsight.datasets import (
    bundles2channels,
    load_afq_data,
    download_sarica,
    download_weston_havens,
    AFQDataset,
    standardize_subject_id,
)

data_path = op.join(afqi.__path__[0], "data")
test_data_path = op.join(data_path, "test_data")


def test_bundles2channels():
    X0 = np.random.rand(50, 4000)
    X1 = bundles2channels(X0, n_nodes=100, n_channels=40, channels_last=True)
    assert X1.shape == (50, 100, 40)
    assert np.allclose(X0[:, :100], X1[:, :, 0])

    X1 = bundles2channels(X0, n_nodes=100, n_channels=40, channels_last=False)
    assert X1.shape == (50, 40, 100)
    assert np.allclose(X0[:, :100], X1[:, 0, :])

    with pytest.raises(ValueError):
        bundles2channels(X0, n_nodes=1000, n_channels=7)


def test_standardize_subject_id():
    assert standardize_subject_id("sub-01") == "sub-01"
    assert standardize_subject_id("01") == "sub-01"


def test_afqdataset_label_encode():
    sub_dicts = [
        {"subject_id": "1", "age": 0, "site": "A"},
        {"subject_id": "2", "age": 1, "site": "B"},
        {"subject_id": "3", "age": 2},
    ]
    node_dicts = [
        {"subjectID": "sub-1", "tractID": "A", "nodeID": 0, "fa": 0.1},
        {"subjectID": "sub-1", "tractID": "A", "nodeID": 1, "fa": 0.2},
        {"subjectID": "sub-1", "tractID": "B", "nodeID": 0, "fa": 0.3},
        {"subjectID": "sub-1", "tractID": "B", "nodeID": 1, "fa": 0.3},
        {"subjectID": "sub-2", "tractID": "A", "nodeID": 0, "fa": 0.4},
        {"subjectID": "sub-2", "tractID": "A", "nodeID": 1, "fa": 0.5},
        {"subjectID": "sub-2", "tractID": "B", "nodeID": 0, "fa": 0.6},
        {"subjectID": "sub-2", "tractID": "B", "nodeID": 1, "fa": 0.6},
        {"subjectID": "3", "tractID": "A", "nodeID": 0, "fa": 0.7},
        {"subjectID": "3", "tractID": "A", "nodeID": 1, "fa": 0.8},
        {"subjectID": "3", "tractID": "B", "nodeID": 0, "fa": 0.9},
        {"subjectID": "3", "tractID": "B", "nodeID": 1, "fa": 0.9},
    ]
    subs = pd.DataFrame(sub_dicts)
    nodes = pd.DataFrame(node_dicts)

    with tempfile.TemporaryDirectory() as temp_dir:
        subs.to_csv(op.join(temp_dir, "subjects.csv"), index=False)
        nodes.to_csv(op.join(temp_dir, "nodes.csv"), index=False)

        tmp_dataset = afqi.AFQDataset(
            fn_nodes=op.join(temp_dir, "nodes.csv"),
            fn_subjects=op.join(temp_dir, "subjects.csv"),
            target_cols=["site"],
            dwi_metrics=["fa"],
            index_col="subject_id",
            label_encode_cols=["site"],
        )

        assert tmp_dataset.y.shape == (3,)
        tmp_dataset.drop_target_na()
        assert tmp_dataset.y.shape == (2,)

        tmp_dataset = afqi.AFQDataset(
            fn_nodes=op.join(temp_dir, "nodes.csv"),
            fn_subjects=op.join(temp_dir, "subjects.csv"),
            target_cols=["age", "site"],
            dwi_metrics=["fa"],
            index_col="subject_id",
            label_encode_cols=["site"],
        )

        assert tmp_dataset.y.shape == (3, 2)
        tmp_dataset.drop_target_na()
        assert tmp_dataset.y.shape == (2, 2)


def test_afqdataset_sub_prefix():
    sub_dicts = [
        {"subject_id": "1", "age": 0},
        {"subject_id": "2", "age": 1},
        {"subject_id": "3", "age": 2},
    ]
    node_dicts = [
        {"subjectID": "sub-1", "tractID": "A", "nodeID": 0, "fa": 0.1},
        {"subjectID": "sub-1", "tractID": "A", "nodeID": 1, "fa": 0.2},
        {"subjectID": "sub-1", "tractID": "B", "nodeID": 0, "fa": 0.3},
        {"subjectID": "sub-1", "tractID": "B", "nodeID": 1, "fa": 0.3},
        {"subjectID": "sub-2", "tractID": "A", "nodeID": 0, "fa": 0.4},
        {"subjectID": "sub-2", "tractID": "A", "nodeID": 1, "fa": 0.5},
        {"subjectID": "sub-2", "tractID": "B", "nodeID": 0, "fa": 0.6},
        {"subjectID": "sub-2", "tractID": "B", "nodeID": 1, "fa": 0.6},
        {"subjectID": "3", "tractID": "A", "nodeID": 0, "fa": 0.7},
        {"subjectID": "3", "tractID": "A", "nodeID": 1, "fa": 0.8},
        {"subjectID": "3", "tractID": "B", "nodeID": 0, "fa": 0.9},
        {"subjectID": "3", "tractID": "B", "nodeID": 1, "fa": 0.9},
    ]
    subs = pd.DataFrame(sub_dicts)
    nodes = pd.DataFrame(node_dicts)

    with tempfile.TemporaryDirectory() as temp_dir:
        subs.to_csv(op.join(temp_dir, "subjects.csv"), index=False)
        nodes.to_csv(op.join(temp_dir, "nodes.csv"), index=False)

        tmp_dataset = afqi.AFQDataset(
            fn_nodes=op.join(temp_dir, "nodes.csv"),
            fn_subjects=op.join(temp_dir, "subjects.csv"),
            target_cols=["age"],
            dwi_metrics=["fa"],
            index_col="subject_id",
        )

    assert set(tmp_dataset.subjects) == set([f"sub-{i}" for i in range(1, 4)])
    assert tmp_dataset.X.shape == (3, 4)
    assert tmp_dataset.y.shape == (3,)
    assert np.isnan(tmp_dataset.y).sum() == 0


@pytest.mark.parametrize("target_cols", [["class"], ["age", "class"]])
def test_AFQDataset(target_cols):
    sarica_dir = download_sarica()
    afq_data = AFQDataset(
        fn_nodes=op.join(sarica_dir, "nodes.csv"),
        fn_subjects=op.join(sarica_dir, "subjects.csv"),
        dwi_metrics=["md", "fa"],
        target_cols=target_cols,
        label_encode_cols=["class"],
    )

    y_shape = (48, 2) if len(target_cols) == 2 else (48,)

    assert afq_data.X.shape == (48, 4000)  # nosec
    assert afq_data.y.shape == y_shape  # nosec
    assert len(afq_data.groups) == 40  # nosec
    assert len(afq_data.feature_names) == 4000  # nosec
    assert len(afq_data.group_names) == 40  # nosec
    assert len(afq_data.subjects) == 48  # nosec
    assert afq_data.bundle_means().shape == (48, 40)  # nosec

    # Test pytorch dataset method

    pt_dataset = afq_data.as_torch_dataset()
    assert len(pt_dataset) == 48
    assert pt_dataset.X.shape == (48, 40, 100)  # nosec
    assert pt_dataset.y.shape == y_shape  # nosec
    assert np.allclose(
        pt_dataset[0][0][0], afq_data.X[0, :100], equal_nan=True
    )  # nosec

    pt_dataset = afq_data.as_torch_dataset(channels_last=True)
    assert len(pt_dataset) == 48
    assert pt_dataset.X.shape == (48, 100, 40)  # nosec
    assert pt_dataset.y.shape == y_shape  # nosec
    assert np.allclose(
        pt_dataset[0][0][:, 0], afq_data.X[0, :100], equal_nan=True
    )  # nosec

    pt_dataset = afq_data.as_torch_dataset(bundles_as_channels=False)
    assert len(pt_dataset) == 48
    assert pt_dataset.X.shape == (48, 4000)  # nosec
    assert pt_dataset.y.shape == y_shape  # nosec
    assert np.allclose(pt_dataset[0][0], afq_data.X[0], equal_nan=True)  # nosec

    # Test tensorflow dataset method

    tf_dataset = list(afq_data.as_tensorflow_dataset().as_numpy_iterator())
    assert len(tf_dataset) == 48
    assert np.allclose(
        tf_dataset[0][0][:, 0], afq_data.X[0, :100], equal_nan=True
    )  # nosec

    tf_dataset = list(
        afq_data.as_tensorflow_dataset(channels_last=False).as_numpy_iterator()
    )
    assert len(tf_dataset) == 48
    assert np.allclose(
        tf_dataset[0][0][0], afq_data.X[0, :100], equal_nan=True
    )  # nosec

    tf_dataset = list(
        afq_data.as_tensorflow_dataset(bundles_as_channels=False).as_numpy_iterator()
    )
    assert len(tf_dataset) == 48
    assert np.allclose(tf_dataset[0][0], afq_data.X[0], equal_nan=True)  # nosec

    # Test the drop_target_na method
    if len(target_cols) == 2:
        afq_data.y[0, 0] = np.nan
        y_shape = (47, 2)
    else:
        afq_data.y[0] = np.nan
        y_shape = (47,)

    afq_data.drop_target_na()
    assert afq_data.X.shape == (47, 4000)  # nosec
    assert afq_data.y.shape == y_shape  # nosec
    assert len(afq_data.subjects) == 47  # nosec

    # Do it all again for an unsupervised dataset

    afq_data = AFQDataset(
        fn_nodes=op.join(sarica_dir, "nodes.csv"),
        fn_subjects=op.join(sarica_dir, "subjects.csv"),
        dwi_metrics=["md", "fa"],
        unsupervised=True,
    )

    assert afq_data.X.shape == (48, 4000)  # nosec
    assert afq_data.y is None  # nosec
    assert len(afq_data.groups) == 40  # nosec
    assert len(afq_data.feature_names) == 4000  # nosec
    assert len(afq_data.group_names) == 40  # nosec
    assert len(afq_data.subjects) == 48  # nosec

    pt_dataset = afq_data.as_torch_dataset()
    assert len(pt_dataset) == 48
    assert pt_dataset.X.shape == (48, 40, 100)  # nosec
    assert torch.all(torch.eq(pt_dataset.y, torch.tensor([])))  # nosec
    assert np.allclose(pt_dataset[0][0], afq_data.X[0, :100], equal_nan=True)  # nosec

    tf_dataset = list(afq_data.as_tensorflow_dataset().as_numpy_iterator())
    assert len(tf_dataset) == 48
    assert np.allclose(
        tf_dataset[0][:, 0], afq_data.X[0, :100], equal_nan=True
    )  # nosec

    # Test the drop_target_na method does nothing in the unsupervised case
    afq_data.drop_target_na()
    assert afq_data.X.shape == (48, 4000)  # nosec
    assert afq_data.y is None  # nosec
    assert len(afq_data.subjects) == 48  # nosec


@pytest.mark.parametrize("dwi_metrics", [["md", "fa"], None])
@pytest.mark.parametrize("enforce_sub_prefix", [True, False])
def test_fetch(dwi_metrics, enforce_sub_prefix):
    sarica_dir = download_sarica()

    with pytest.raises(ValueError):
        load_afq_data(
            fn_nodes=op.join(sarica_dir, "nodes.csv"),
            fn_subjects=op.join(sarica_dir, "subjects.csv"),
            dwi_metrics=dwi_metrics,
            target_cols=["class"],
            label_encode_cols=["class"],
            concat_subject_session=True,
        )

    X, y, groups, feature_names, group_names, subjects, _, _ = load_afq_data(
        fn_nodes=op.join(sarica_dir, "nodes.csv"),
        fn_subjects=op.join(sarica_dir, "subjects.csv"),
        dwi_metrics=dwi_metrics,
        target_cols=["class"],
        label_encode_cols=["class"],
        enforce_sub_prefix=enforce_sub_prefix,
    )

    n_features = 16000 if dwi_metrics is None else 4000
    n_groups = 160 if dwi_metrics is None else 40

    assert X.shape == (48, n_features)  # nosec
    assert y.shape == (48,)  # nosec
    assert len(groups) == n_groups  # nosec
    assert len(feature_names) == n_features  # nosec
    assert len(group_names) == n_groups  # nosec
    assert len(subjects) == 48  # nosec
    assert op.isfile(
        op.join(afqi.datasets._DATA_DIR, "sarica_data", "nodes.csv")
    )  # nosec
    assert op.isfile(
        op.join(afqi.datasets._DATA_DIR, "sarica_data", "subjects.csv")
    )  # nosec

    wh_dir = download_weston_havens()
    X, y, groups, feature_names, group_names, subjects, _, _ = load_afq_data(
        fn_nodes=op.join(wh_dir, "nodes.csv"),
        fn_subjects=op.join(wh_dir, "subjects.csv"),
        dwi_metrics=dwi_metrics,
        target_cols=["Age"],
    )

    n_features = 10000 if dwi_metrics is None else 4000
    n_groups = 100 if dwi_metrics is None else 40

    assert X.shape == (77, n_features)  # nosec
    assert y.shape == (77,)  # nosec
    assert len(groups) == n_groups  # nosec
    assert len(feature_names) == n_features  # nosec
    assert len(group_names) == n_groups  # nosec
    assert len(subjects) == 77  # nosec
    assert op.isfile(
        op.join(afqi.datasets._DATA_DIR, "weston_havens_data", "nodes.csv")
    )  # nosec
    assert op.isfile(
        op.join(afqi.datasets._DATA_DIR, "weston_havens_data", "subjects.csv")
    )  # nosec

    with tempfile.TemporaryDirectory() as td:
        _ = download_sarica(data_home=td)
        _ = download_weston_havens(data_home=td)
        assert op.isfile(op.join(td, "sarica_data", "nodes.csv"))  # nosec
        assert op.isfile(op.join(td, "sarica_data", "subjects.csv"))  # nosec
        assert op.isfile(op.join(td, "weston_havens_data", "nodes.csv"))  # nosec
        assert op.isfile(op.join(td, "weston_havens_data", "subjects.csv"))  # nosec


def test_load_afq_data_smoke():
    output = load_afq_data(
        fn_nodes=op.join(test_data_path, "nodes.csv"),
        fn_subjects=op.join(test_data_path, "subjects.csv"),
        target_cols=["test_class"],
        label_encode_cols=["test_class"],
    )
    assert len(output) == 8  # nosec

    output = load_afq_data(
        fn_nodes=op.join(test_data_path, "nodes.csv"),
        fn_subjects=op.join(test_data_path, "subjects.csv"),
        target_cols=["test_class"],
        label_encode_cols=["test_class"],
        unsupervised=True,
    )
    assert len(output) == 8  # nosec
    assert output.y is None  # nosec
    assert output.classes is None  # nosec

    output = load_afq_data(
        fn_nodes=op.join(test_data_path, "nodes.csv"),
        fn_subjects=op.join(test_data_path, "subjects.csv"),
        target_cols=["test_class"],
        label_encode_cols=["test_class"],
        unsupervised=True,
    )
    assert len(output) == 8  # nosec
    assert output.y is None  # nosec
    assert output.classes is None  # nosec


@pytest.mark.parametrize("dwi_metrics", [["volume", "md"], None])
def test_load_afq_data(dwi_metrics):
    (X, y, groups, feature_names, group_names, subjects, _, classes) = load_afq_data(
        fn_nodes=op.join(test_data_path, "nodes.csv"),
        fn_subjects=op.join(test_data_path, "subjects.csv"),
        dwi_metrics=dwi_metrics,
        target_cols=["test_class"],
        label_encode_cols=["test_class"],
        return_bundle_means=False,
        enforce_sub_prefix=False,
    )

    nodes = pd.read_csv(op.join(test_data_path, "nodes.csv"))
    X_ref = np.load(op.join(test_data_path, "test_transform_x.npy"))
    y_ref = np.load(op.join(test_data_path, "test_data_y.npy"))
    groups_ref = np.load(op.join(test_data_path, "test_transform_groups.npy"))
    cols_ref = [
        tuple(item)
        for item in np.load(op.join(test_data_path, "test_transform_cols.npy"))
    ]

    assert np.allclose(X, X_ref, equal_nan=True)  # nosec
    assert np.allclose(y, y_ref)  # nosec
    assert np.allclose(groups, groups_ref)  # nosec
    assert feature_names == cols_ref  # nosec
    assert group_names == [tup[0:2] for tup in cols_ref if tup[2] == 0]  # nosec
    assert set(subjects) == set(nodes.subjectID.unique())  # nosec
    assert all(classes["test_class"] == np.array(["c0", "c1"]))  # nosec

    (X, y, groups, feature_names, group_names, subjects, _, classes) = load_afq_data(
        fn_nodes=op.join(test_data_path, "nodes.csv"),
        fn_subjects=op.join(test_data_path, "subjects.csv"),
        dwi_metrics=dwi_metrics,
        target_cols=["test_class"],
        label_encode_cols=["test_class"],
        return_bundle_means=True,
        enforce_sub_prefix=False,
    )

    means_ref = (
        nodes.groupby(["subjectID", "tractID"])
        .agg("mean")
        .drop("nodeID", axis="columns")
        .unstack("tractID")
    )
    assert np.allclose(X, means_ref.to_numpy(), equal_nan=True)  # nosec
    assert group_names == means_ref.columns.to_list()  # nosec
    assert feature_names == means_ref.columns.to_list()  # nosec
    assert set(subjects) == set(nodes.subjectID.unique())  # nosec

    with pytest.raises(ValueError):
        load_afq_data(
            fn_nodes=op.join(test_data_path, "nodes.csv"),
            fn_subjects=op.join(test_data_path, "subjects.csv"),
            target_cols=["test_class"],
            label_encode_cols=["test_class", "error"],
        )
    with pytest.raises(ValueError) as ee:
        load_afq_data(
            fn_nodes=op.join(test_data_path, "nodes.csv"),
            fn_subjects=op.join(test_data_path, "subjects.csv"),
        )

    assert "please set `unsupervised=True`" in str(ee.value)  # nosec
