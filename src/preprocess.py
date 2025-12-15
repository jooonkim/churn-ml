"""Preprocessing utilities built around sklearn's ColumnTransformer."""
from typing import Any


def build_preprocessor(categorical_features: list[str], numeric_features: list[str]) -> Any:
    """Create and return a ColumnTransformer with appropriate pipelines.

    Placeholder: add encoders for categorical columns and scalers/imputers for numeric columns.
    When implementing, explain why each transformer is chosen and how it affects the model.
    """
    raise NotImplementedError("Implement ColumnTransformer assembly")
