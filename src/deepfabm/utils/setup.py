from argparse import Namespace

from .logger import LOGGER, setup_logging, setup_wandb, terminate_wandb
from .seed import set_seed


def initialize_run(setup: Namespace) -> None:
    """
    Initializes run by setting up results directory and initializing all services.
    Adjusts namespace in place to contain information on the initialized assets.

    :param script: Invoked script, either `"train"` or `"evaluate"`
    :type script: str
    :param setup: Experimental setup
    :type setup: Namespace
    """
    # Set up logging
    setup_logging(setup.loglevel)
    LOGGER.info(f"Dictionary of parsed arguments: {vars(setup)!r}")

    # Set up Weights & Biases logging
    if setup.wandb:
        setup_wandb(project=setup.wandb, config=vars(setup))
    else:
        LOGGER.info("Skipping Weights & Biases initialization.")

    # Set up the random seed
    set_seed(setup.seed)

    return setup


def terminate_run(parsed_args: Namespace):
    """
    Finalizes run by stopping all running services.

    :param setup: Experimental setup
    :type setup: Namespace
    """
    # Terminate Weights & Biases logging
    if parsed_args.wandb:
        terminate_wandb()
