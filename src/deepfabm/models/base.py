from abc import ABC, abstractmethod
from collections.abc import Mapping
from types import MappingProxyType

import numpy as np


class Model(ABC):
    """Abstract base class for all model implementations."""

    # Named sets of parameters for model implementation
    _PARAMETRIZATIONS: Mapping[str, Mapping[str, float]] = MappingProxyType({})

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

    @classmethod
    def list_parametrizations(cls) -> list[str]:
        """
        List all parametrizations available for the model.

        :return: List of all available parametrization identifiers
        :rtype: list[str]
        """
        return sorted(cls._PARAMETRIZATIONS)

    @classmethod
    def get_parameters(cls, parametrization: str) -> dict[str, float]:
        """
        Retrieve model parameters based on the model parametrization.

        :param parametrization: Parametrization identifier
        :type parametrization: str
        :return: Dictionary of parameters and their values
        :rtype: dict[str, float]
        """
        try:
            parameters = cls._PARAMETRIZATIONS[parametrization]
        except KeyError as e:
            raise ValueError(
                f"No parametrization found for {parametrization!r}. \
                    Available: {cls.list_parametrizations()}."
            ) from e

        # Make a copy to ensure the class-level mapping is not changed
        return dict(parameters)
