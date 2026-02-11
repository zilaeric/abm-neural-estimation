from abc import ABC, abstractmethod


class Network(ABC):
    """Abstract base class for all neural network implementations."""

    @abstractmethod
    def forward(self, *args, **kwargs):
        """
        Run a forward pass.

        Concrete networks must implement this method.
        """
        raise NotImplementedError
