from deepabm.utils import LOGGER


def load_model(model: str):
    """
    Load the specified model.

    Args:
        model: The model to load.

    Returns:
        The loaded model.
    """
    LOGGER.info(f"Loading the '{model}' model...")

    # Switch to chosen model
    if model == "cdt":
        # TODO Implement Central Decision Transformer (IDT) model
        raise NotImplementedError("The 'cdt' model is not yet implemented!")
    elif model == "idt":
        # TODO Implement Independent Decision Transformer (IDT) model
        raise NotImplementedError("The 'idt' model is not yet implemented!")
    elif model == "kddt":
        # TODO Implement Knowledge Distillation Decision Transformer (KDDT) model
        raise NotImplementedError("The 'kddt' model is not yet implemented!")
    else:
        LOGGER.error(f"Attempted to load an invalid model: '{model}'!")
        raise ValueError(f"Attempted to load an invalid model: '{model}'!")
