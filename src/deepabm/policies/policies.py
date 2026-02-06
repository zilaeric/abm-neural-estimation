from .policy_astar import AStarPolicy
from .policy_random import RandomPolicy
from .policy_trained import TrainedPolicy

from deepabm.utils import LOGGER

def load_policy(policy: str):
    """
    Load the specified policy.

    Args:
        policy: The policy to load.

    Returns:
        The loaded policy
    """
    LOGGER.info(f"Loading the '{policy}' policy...")

    # Switch to chosen policy
    if policy == "random":
        return RandomPolicy()
    elif policy == "astar":
        return AStarPolicy()
    elif policy == "trained":
        return TrainedPolicy()
    else:
        LOGGER.error(f"Attempted to load an invalid policy: '{policy}'!")
        raise ValueError(f"Attempted to load an invalid policy: '{policy}'!")
