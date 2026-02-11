from abc import ABC, abstractmethod

import numpy as np


class Model(ABC):
    """Abstract base class for all model implementations."""

    @abstractmethod
    def generate(self, parameters: np.ndarray) -> np.ndarray:
        """
        Use the model to generate a time-series given the set of model parameters.

        :param parameters: Model parameters to set when generating time-series
        :type parameters: np.ndarray
        :return: One time-series generated using the model
        :rtype: ndarray
        """
        raise NotImplementedError
