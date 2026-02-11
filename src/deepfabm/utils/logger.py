import logging
import sys

LOGGER = logging.getLogger(__name__)


def setup_logging(loglevel: int | str) -> None:
    """
    Set up logging configuration.

    :param loglevel: Level of logs to print out
    :type loglevel: int | str
    """
    logformat = "[%(asctime)s] %(levelname)s: %(message)s"
    logging.basicConfig(
        level=loglevel, stream=sys.stdout, format=logformat, datefmt="%Y-%m-%d %H:%M:%S"
    )


def setup_wandb(project: str = "deepabm", config: dict = None) -> None:
    """
    Initiate Weights & Biases logging.

    :param project: W&B project name to pass results to
    :type project: str
    :param config: Training configuration to save in the W&B project
    :type config: dict
    """
    import wandb

    wandb.init(project=project, config=config)
    LOGGER.info(f"Weights & Biases logging initialized under '{project}' project.")


def terminate_wandb() -> None:
    """
    Terminate Weights & Biases logging.
    """
    import wandb

    wandb.finish()
    LOGGER.info("Weights & Biases logging terminated.")
