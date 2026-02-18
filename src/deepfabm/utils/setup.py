import os
from argparse import Namespace
from datetime import datetime

from .logger import LOGGER, setup_logging, setup_wandb, terminate_wandb
from .seed import set_seed


def _prepare_results_dir(setup: Namespace) -> None:
    """
    Create directory to store experiment results in. Reusable paths are saved to the
    experimental setup namespace passed as `setup`.

    :param setup: Experimental setup
    :type setup: Namespace
    """
    # Create unique identifier for the current experiment
    id = f"experiment_{datetime.now().strftime('%Y-%m-%mT%H:%M:%S')}"

    # Create experiment results directory
    resultsdir = os.path.join("results", id)
    os.mkdir(resultsdir)

    # Save path to results directory to experimental setup
    setup.resultsdir = resultsdir


def initialize_run(setup: Namespace) -> None:
    """
    Initializes run by setting up results directory and initializing all services.
    Adjusts namespace in place to contain information on the initialized assets.

    :param script: Invoked script, either `"train"` or `"evaluate"`
    :type script: str
    :param setup: Experimental setup
    :type setup: Namespace
    """
    # Set up experimental results folder
    if setup.command == "train":
        _prepare_results_dir(setup)

    # Set up logging
    setup_logging(setup.loglevel)
    LOGGER.info(f"Dictionary of parsed arguments: {vars(setup)!r}")

    # Set up Weights & Biases logging
    if setup.wandb:
        setup_wandb(project=setup.wandb, config=vars(setup))
    else:
        LOGGER.info("Skipping Weights & Biases initialization.")

    # Set random seed
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
