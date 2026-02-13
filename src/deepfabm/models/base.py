from abc import ABC, abstractmethod

import numpy as np


class Model(ABC):
    """Abstract base class for all model implementations."""

    @abstractmethod
    def generate(self, parameters: dict, obs: int, burn: int, batch: int) -> np.ndarray:
        """
        Use the model to generate time-series given the set of model parameters.

        :param parameters: Dictionary of model parameters to set when generating series
        :type parameters: dict
        :param obs: Number of observations
        :type obs: int
        :param burn: Burn-in period length
        :type burn: int
        :param batch: Number of generated series
        :type batch: int
        :return: Generated series matrix of dimensions `[batch, obs]`
        :rtype: ndarray
        """
        raise NotImplementedError
