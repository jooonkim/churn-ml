"""PyTorch model definitions and helpers."""
import torch


class SimpleTorchModel(torch.nn.Module):
    """Placeholder feedforward network. Customize architecture as you learn."""

    def __init__(self, input_dim: int, hidden_dim: int = 64, output_dim: int = 1):
        super().__init__()
        # Replace with real layers during implementation.
        self.model = torch.nn.Identity()

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        return self.model(x)
