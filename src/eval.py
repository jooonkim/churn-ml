"""Evaluation helpers for sklearn and torch models."""
from typing import Any, Dict


def evaluate_classification(y_true: Any, y_pred: Any, y_proba: Any | None = None) -> Dict[str, float]:
    """Compute core metrics like accuracy, precision, recall, F1, AUC.

    Placeholder: call sklearn.metrics functions and return a metrics dictionary.
    """
    raise NotImplementedError("Implement evaluation metrics")
