import numpy as np

from ..base import Model
from ..registry import register_model


@register_model("rwalkd")
class RandomWalkDrift(Model):
    """Random walk with a drift."""

    def generate(self, parameters: dict, obs: int, burn: int, batch: int) -> np.ndarray:
        # Retrieve parameters from parameter array
        d = parameters["d"]

        # Calculate total number of observations to generate including burn-in period
        total = obs + burn

        # Generate error term and drift constant for all observations
        errors = np.random.randn(batch, total)
        drifts = np.full((batch, total), d, dtype=np.float64)

        # Calculate final series and log returns
        price = np.cumsum(drifts + errors, axis=1)
        returns = np.diff(np.log(price), prepend=0)

        # Cut out burn-in period and return requested number of observations
        return returns[:, -obs:]
