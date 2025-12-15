"""Data loading utilities: fetch OpenML dataset and split into train/val/test."""
from typing import Tuple


def load_data(dataset_name: str, test_size: float = 0.2, val_size: float = 0.1, random_state: int = 42) -> Tuple[object, object, object, object]:
    """Fetch dataset via OpenML, then return (X_train, X_val, X_test, y variants).

    Placeholder: use sklearn.datasets.fetch_openml, then train/val/test split.
    Over-explain steps when implemented so future readers learn why each choice matters.
    """
    raise NotImplementedError("Implement fetch_openml download + split logic")
