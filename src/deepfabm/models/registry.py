from .base import Model
from .implementations.rwalksb import RandomWalkWithStructuralBreak

from deepfabm.utils import LOGGER


_MODEL_REGISTRY = {}


def register_model(name: str):
    def decorator(cls: Model) -> Model:
        if name in _MODEL_REGISTRY and _MODEL_REGISTRY[name] is not cls:
            raise ValueError(f"Model '{name}' already registered")
        
        _MODEL_REGISTRY[name] = cls
        return cls
    
    return decorator


def load_model(model: str, **kwargs) -> Model:
    """
    Load specified model.
    
    :param model: Model identifier
    :type model: str
    :return: Model instance
    :rtype: Model
    """
    from . import implementations

    # Retrieve correct model
    try:
        cls = _MODEL_REGISTRY[model]
    except KeyError as e:
        raise ValueError(
            f"No model found for '{model}'. Available: {sorted(_MODEL_REGISTRY)}."
        ) from e
    if model in _MODEL_REGISTRY:
        return _MODEL_REGISTRY[model](**kwargs)
    
    return cls(**kwargs)
