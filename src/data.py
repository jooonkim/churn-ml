"""Data loading utilities: fetch OpenML dataset and split into train/val/test."""
from typing import Tuple
from sklearn.datasets import fetch_openml

def load_data(dataset_id: int, test_size: float = 0.2, val_size: float = 0.1, random_state: int = 42) -> Tuple[object, object, object, object]:
    """Fetch dataset via OpenML, then return (X_train, X_val, X_test, y variants).

    Placeholder: use sklearn.datasets.fetch_openml, then train/val/test split.
    Over-explain steps when implemented so future readers learn why each choice matters.
    """
    # Download the raw table from OpenML to understand the dataset
    churn_data = fetch_openml(data_id=45568)

    # raise NotImplementedError("Implement fetch_openml download + split logic")

data = load_data(45568)