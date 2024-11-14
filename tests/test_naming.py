import unittest
from biocore.utils.naming import (
    camelcase_to_snakecase,
    snakecase_to_camelcase,
    filename_prefix_for_name,
    filename_prefix_for_split,
    filepattern_for_dataset_split,
    filenames_for_dataset_split,
)


class TestNamingUtils(unittest.TestCase):
    def test_camelcase_to_snakecase(self):
        self.assertEqual(camelcase_to_snakecase("CamelCase"), "camel_case")
        self.assertEqual(camelcase_to_snakecase("camelCase"), "camel_case")
        self.assertEqual(camelcase_to_snakecase("CamelCamelCase"), "camel_camel_case")
        self.assertEqual(
            camelcase_to_snakecase("Camel2Camel2Case"), "camel2_camel2_case"
        )

    def test_snakecase_to_camelcase(self):
        self.assertEqual(snakecase_to_camelcase("snake_case"), "SnakeCase")
        self.assertEqual(
            snakecase_to_camelcase("snake_case_example"), "SnakeCaseExample"
        )

    def test_filename_prefix_for_name(self):
        self.assertEqual(filename_prefix_for_name("DatasetName"), "dataset_name")
        with self.assertRaises(ValueError):
            filename_prefix_for_name("path/to/DatasetName")

    def test_filename_prefix_for_split(self):
        self.assertEqual(
            filename_prefix_for_split("DatasetName", "split"), "dataset_name-split"
        )
        with self.assertRaises(ValueError):
            filename_prefix_for_split("path/to/DatasetName", "split")
        with self.assertRaises(ValueError):
            filename_prefix_for_split("DatasetName", "invalid split")

    def test_filepattern_for_dataset_split(self):
        self.assertEqual(
            filepattern_for_dataset_split("DatasetName", "split", "/data"),
            "/data/dataset_name-split*",
        )
        self.assertEqual(
            filepattern_for_dataset_split("DatasetName", "split", "/data", "suffix"),
            "/data/dataset_name-split.suffix*",
        )

    def test_filenames_for_dataset_split(self):
        self.assertEqual(
            filenames_for_dataset_split("/data", "DatasetName", "split"),
            ["/data/dataset_name-split"],
        )
        self.assertEqual(
            filenames_for_dataset_split("/data", "DatasetName", "split", "suffix"),
            ["/data/dataset_name-split.suffix"],
        )
        self.assertEqual(
            filenames_for_dataset_split(
                "/data", "DatasetName", "split", shard_lengths=[1, 2, 3]
            ),
            [
                "/data/dataset_name-split-00000-of-00003",
                "/data/dataset_name-split-00001-of-00003",
                "/data/dataset_name-split-00002-of-00003",
            ],
        )
        self.assertEqual(
            filenames_for_dataset_split(
                "/data", "DatasetName", "split", "suffix", shard_lengths=[1, 2, 3]
            ),
            [
                "/data/dataset_name-split-00000-of-00003.suffix",
                "/data/dataset_name-split-00001-of-00003.suffix",
                "/data/dataset_name-split-00002-of-00003.suffix",
            ],
        )


if __name__ == "__main__":
    unittest.main()
