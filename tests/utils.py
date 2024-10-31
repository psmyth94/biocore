import unittest

from biocore.utils.import_util import (
    is_biosets_available,
    is_datasets_available,
    is_polars_available,
)


def require_datasets(test_case):
    """
    Decorator marking a test that requires Datasets.

    These tests are skipped when Datasets isn't installed.

    """
    if not is_datasets_available():
        test_case = unittest.skip("test requires Datasets")(test_case)
    return test_case


def require_biosets(test_case):
    """
    Decorator marking a test that requires Biosets.

    These tests are skipped when Biosets isn't installed.

    """
    if not is_biosets_available():
        test_case = unittest.skip("test requires Biosets")(test_case)
    return test_case


def require_polars(test_case):
    """
    Decorator marking a test that requires Polars.

    These tests are skipped when Polars isn't installed.

    """
    if not is_polars_available():
        test_case = unittest.skip("test requires Polars")(test_case)
    return test_case
