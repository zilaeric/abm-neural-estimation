from __future__ import annotations

from .base import Model

from deepfabm.utils import LOGGER


_MODEL_REGISTRY: dict[str, type[Model]] = {}
_IMPLEMENTATIONS_IMPORTED: bool = False


def _register_implementations() -> None:
    """
    Ensure all model implementations have been imported at least once.

    Importing the implementations package triggers decorator-based registration.
    This function is safe to call multiple times.
    """
    global _IMPLEMENTATIONS_IMPORTED
    if _IMPLEMENTATIONS_IMPORTED:
        return

    from . import implementations  # noqa: F401
    _IMPLEMENTATIONS_IMPORTED = True

    LOGGER.debug(f"Model registry contains the following models: {list_models()}.")


def register_model(name: str):
    """
    Class decorator to register a model implementation.
    
    :param name: Model identifier to use for the model class
    :type name: str
    """
    def decorator(model_class: type[Model]) -> type[Model]:
        if name in _MODEL_REGISTRY and _MODEL_REGISTRY[name] is not model_class:
            raise ValueError(f"Model '{name}' already registered.")

        if not issubclass(model_class, Model):
            raise TypeError(
                f"Trying to add model '{name}' which is not subclass of the 'Model' class."
            )

        # Add model to model registry
        _MODEL_REGISTRY[name] = model_class
        
        return model_class
    
    return decorator


def list_models() -> list[str]:
    """
    List all models registered in the model registry.
    
    :return: List of all identifiers from the model registry
    :rtype: list[str]
    """
    _register_implementations()

    return sorted(_MODEL_REGISTRY)


def load_model(model: str, **kwargs) -> Model:
    """
    Load specified model. Preferred way of loading models.
    
    :param model: Model identifier of the model to be loaded
    :type model: str
    :return: Instance of the loaded model
    :rtype: Model
    """
    _register_implementations()

    try:
        model_class = _MODEL_REGISTRY[model]
        LOGGER.info(f"Loaded model '{model}' from model registry.")
    except KeyError as e:
        raise ValueError(
            f"No model found for '{model}'. Available: {list_models()}."
        ) from e
    
    return model_class(**kwargs)
