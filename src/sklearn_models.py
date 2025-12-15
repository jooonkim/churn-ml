"""Factory functions for sklearn models (e.g., logistic regression, random forest)."""
from typing import Any


def build_logistic_regression(*, class_weight: str | dict | None = None, max_iter: int = 1000) -> Any:
    """Return an un-fitted logistic regression model.

    Placeholder: initialize sklearn.linear_model.LogisticRegression with sensible defaults.
    Over-explain hyperparameters when implemented.
    """
    raise NotImplementedError("Implement logistic regression factory")


def build_random_forest(*, random_state: int = 42, class_weight: str | dict | None = None) -> Any:
    """Return an un-fitted random forest classifier.

    Placeholder: initialize sklearn.ensemble.RandomForestClassifier.
    """
    raise NotImplementedError("Implement random forest factory")
