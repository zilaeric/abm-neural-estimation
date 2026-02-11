from ..base import Model
from ..registry import register_model

import numpy as np

@register_model("rwalksb")
class RandomWalkWithStructuralBreak(Model):
    def __init__(self):
        super().__init__()

    def generate(self, parameters: np.ndarray) -> np.ndarray:
        raise NotImplementedError(f"{self.__class__} is missing data generation function!")
