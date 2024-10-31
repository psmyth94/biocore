import tempfile
from pathlib import Path

import numpy as np
import pandas as pd
import pyarrow as pa
import pytest
from biocore.data_handling import DataHandler, _FORMAT_TO_CONVERTER
from tests.utils import require_biosets, require_datasets, require_polars


pytestmark = pytest.mark.unit


@pytest.mark.parametrize("format", _FORMAT_TO_CONVERTER.keys())
def test_numpy_converter(format):
    try:
        assert DataHandler.to_format(np.asarray([1, 2, 3]), format) is not None
    except NotImplementedError:
        pass


@pytest.mark.parametrize("format", _FORMAT_TO_CONVERTER.keys())
def test_list_converter(format):
    try:
        assert DataHandler.to_format([1, 2, 3], format) is not None
    except NotImplementedError:
        pass


@pytest.mark.parametrize("format", _FORMAT_TO_CONVERTER.keys())
def test_dict_converter(format):
    try:
        assert DataHandler.to_format({"a": 1}, format) is not None
    except NotImplementedError:
        pass


@pytest.mark.parametrize("format", _FORMAT_TO_CONVERTER.keys())
def test_pandas_converter(format):
    try:
        assert DataHandler.to_format(pd.DataFrame({"a": [1]}), format) is not None
    except NotImplementedError:
        pass


@require_polars
@pytest.mark.parametrize("format", _FORMAT_TO_CONVERTER.keys())
def test_polars_converter(format):
    import polars as pl

    try:
        assert DataHandler.to_format(pl.DataFrame({"a": [1]}), format) is not None
    except NotImplementedError:
        pass


@pytest.mark.parametrize("format", _FORMAT_TO_CONVERTER.keys())
def test_arrow_converter(format):
    try:
        assert (
            DataHandler.to_format(pa.Table.from_pydict({"a": [1]}), format) is not None
        )
    except NotImplementedError:
        pass


@require_biosets
@pytest.mark.parametrize("format", _FORMAT_TO_CONVERTER.keys())
def test_dataset_converter(format):
    from biosets import Bioset

    try:
        kwargs = {}
        if format == "io":
            kwargs["path"] = Path(tempfile.mkdtemp()) / "test_dataset_converter.csv"

        assert (
            DataHandler.to_format(Bioset.from_dict({"a": [1]}), format, **kwargs)
            is not None
        )
    except NotImplementedError:
        pass


@require_datasets
@pytest.mark.parametrize("format", _FORMAT_TO_CONVERTER.keys())
def test_iterable_dataset_converter(format):
    from datasets import IterableDataset

    def gen():
        data = [{"a": 1}]
        for d in data:
            yield d

    try:
        kwargs = {}
        if format == "io":
            kwargs["path"] = Path(tempfile.mkdtemp()) / "test_dataset_converter.csv"
        assert (
            DataHandler.to_format(IterableDataset.from_generator(gen), format, **kwargs)
            is not None
        )
    except NotImplementedError:
        pass
