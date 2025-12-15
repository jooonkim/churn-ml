"""Training loop for sklearn models."""
from typing import Any, Tuple


def train_sklearn_model(model: Any, X_train: Any, y_train: Any, X_val: Any | None = None, y_val: Any | None = None) -> Tuple[Any, dict]:
    """Fit the model and return (fitted_model, metrics_dict).

    Placeholder: fit, then compute simple metrics on validation if provided.
    """
    raise NotImplementedError("Implement sklearn training workflow")
