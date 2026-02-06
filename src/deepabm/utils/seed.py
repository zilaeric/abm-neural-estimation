import random
import numpy as np
import torch


def set_seed(seed):
    """
    Set seed for reproducibility.

    Args:
        seed (int): The seed value to be set.

    Returns:
        None
    """
    random.seed(seed)
    np.random.seed(seed)
    torch.manual_seed(seed)
    torch.cuda.manual_seed_all(seed)
