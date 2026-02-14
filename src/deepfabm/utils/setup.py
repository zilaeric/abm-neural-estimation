import argparse

from .logger import LOGGER, setup_logging, setup_wandb, terminate_wandb
from .parser import EvaluateParser, TrainParser
from .seed import set_seed

_PARSER_MAP = {
    "train": TrainParser,
    "evaluate": EvaluateParser,
}


def initialize_run(
    script: str,
    args: list[str] | argparse.Namespace,
) -> argparse.Namespace:
    """
    Initializes run by setting up results directory and initializing all services.

    :param script: Invoked script, either `"train"` or `"evaluate"`
    :type script: str
    :param args: CLI arguments passed during invocation
    :type args: list[str] | argparse.Namespace
    :return: Parsed arguments
    :rtype: argparse.Namespace
    """
    # Parse the command-line arguments (or reuse an already-parsed Namespace)
    if isinstance(args, argparse.Namespace):
        parsed_args = args
    else:
        if script in _PARSER_MAP:
            parser = _PARSER_MAP[script]()
        else:
            raise ValueError(f"No parser found for the invoked script {script!r}")

        parsed_args = parser.parse_args(args)

    # Set up logging
    setup_logging(parsed_args.loglevel)
    LOGGER.info(f"Dictionary of parsed arguments: {vars(parsed_args)!r}")

    # Set up Weights & Biases logging
    if parsed_args.wandb:
        setup_wandb(project=parsed_args.wandb, config=vars(parsed_args))
    else:
        LOGGER.info("Skipping Weights & Biases initialization.")

    # Set up the random seed
    set_seed(parsed_args.seed)

    return parsed_args


def terminate_run(args: argparse.Namespace):
    """
    Finalizes run by stopping all running services.

    :param args: CLI arguments passed during invocation
    :type args: argparse.Namespace
    """
    # Terminate Weights & Biases logging
    if args.wandb:
        terminate_wandb()
