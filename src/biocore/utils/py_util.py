import sys


def is_dataset_dict(val, iterable=True):
    if iterable:
        return isinstance(val, dict) and all(
            "datasets" in sys.modules
            and isinstance(
                v,
                (
                    sys.modules["datasets"].Dataset,
                    sys.modules["datasets"].IterableDataset,
                ),
            )
            for v in val.values()
        )

    return isinstance(val, dict) and all(
        "datasets" in sys.modules and isinstance(v, sys.modules["datasets"].Dataset)
        for v in val.values()
    )


def is_iterable_dataset(val):
    return "datasets" in sys.modules and isinstance(
        val, sys.modules["datasets"].IterableDataset
    )


def is_dataset(val, iterable=True):
    if iterable:
        return "datasets" in sys.modules and isinstance(
            val,
            (sys.modules["datasets"].Dataset, sys.modules["datasets"].IterableDataset),
        )

    return "datasets" in sys.modules and isinstance(
        val, sys.modules["datasets"].Dataset
    )


def is_bioset(val):
    return "biosets" in sys.modules and isinstance(val, sys.modules["biosets"].Bioset)
