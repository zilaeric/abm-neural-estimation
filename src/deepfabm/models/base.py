from abc import ABC, abstractmethod
import numpy as np


class Model(ABC):
    def __init__(self):
        pass
    
    @abstractmethod
    def generate(self, parameters: np.ndarray) -> np.ndarray:
        pass
