import random
import numpy as np
import torch


def set_seed(seed: int) -> None:
    """
    Set seed to ensure reproducibility of experiments.
    
    :param seed: Seed number
    :type seed: int
    """
    random.seed(seed)
    np.random.seed(seed)
    torch.manual_seed(seed)
    if torch.cuda.is_available():
        torch.cuda.manual_seed_all(seed)
