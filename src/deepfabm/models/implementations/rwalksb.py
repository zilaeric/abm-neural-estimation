import numpy as np

from ..base import Model
from ..registry import register_model


@register_model("rwalksb")
class RandomWalkStructuralBreak(Model):
    """Random walk with a structural break."""

    def generate(self, parameters: dict, obs: int, burn: int, batch: int) -> np.ndarray:
        raise NotImplementedError(f"{self.__class__!r} has not been implemented yet!")
