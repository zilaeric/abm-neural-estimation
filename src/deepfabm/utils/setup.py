import os
from argparse import Namespace
from datetime import datetime

import yaml

from .logger import LOGGER, setup_logging, setup_wandb, terminate_wandb
from .seed import set_seed


def _prepare_results_dir(setup: Namespace) -> None:
    """
    Creates directory to store experiment results in. Reusable paths are saved to the
    experimental setup namespace passed as `setup`.

    :param setup: Experimental setup
    :type setup: Namespace
    """
    # Create unique identifier for the current experiment
    id = f"{setup.experiment}_{datetime.now().strftime('%Y-%m-%mT%H:%M:%S')}"

    # Create experiment results directory
    resultsdir = os.path.join("results", id)
    os.mkdir(resultsdir)
    setup.resultsdir = resultsdir

    # Create trained weights directory
    weightsdir = os.path.join("results", id, "weights")
    os.mkdir(weightsdir)
    setup.weightsdir = weightsdir

    # Create log file
    logpath = os.path.join("results", id, "log.txt")
    open(logpath, "a")
    setup.logpath = logpath


def _merge_configuration(setup: Namespace) -> None:
    """
    Combine experiment configuration such as to respect priority of each source.

    Experimental setup sources take procedence (highest to lowest) as follows:
    1. command-line interface arguments,
    2. named experiment configuration file from the `experiments/` folder, and
    3. default experiment configuration file at 'experiments/default.yaml'.

    :param setup: Experimental setup
    :type setup: Namespace
    """
    # Define paths of files to read experimental configurations from
    experimentpath = os.path.join("experiments", f"{setup.experiment}.yaml")
    defaultpath = os.path.join("experiments", "default.yaml")

    # Add configurations to experimental setup if not set
    for source in [experimentpath, defaultpath]:
        with open(source, "r") as f:
            config = yaml.safe_load(f)
            for arg in config:
                if arg not in setup:
                    setattr(setup, arg, config[arg])


def _save_configuration(setup: Namespace) -> None:
    """
    Saves experimental setup passed as `setup` to the designated experiment results
    folder in the `config.yaml` file.

    :param setup: Experimental setup
    :type setup: Namespace
    """
    configpath = os.path.join(setup.resultsdir, "config.yaml")
    with open(configpath, "a") as f:
        yaml.safe_dump(vars(setup), f)


def initialize_run(setup: Namespace) -> None:
    """
    Initializes run by setting up results directory and initializing all services.
    Adjusts namespace in place to contain information on the initialized assets.

    :param setup: Experimental setup
    :type setup: Namespace
    """
    # Set up experiment results folder
    if setup.command == "train":
        _prepare_results_dir(setup)

    # Finalize configuration
    if setup.command == "train":
        _merge_configuration(setup)
        _save_configuration(setup)

    # Set up logging
    setup_logging(setup.loglevel, getattr(setup, "logpath", None))
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
