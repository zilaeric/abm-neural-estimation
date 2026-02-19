import logging
import sys

LOGGER = logging.getLogger(__name__)


def setup_logging(level: int | str, filename: str | None) -> None:
    """
    Set up logging configuration.

    :param level: Level of logs to print out
    :type level: int | str
    :param filename: Path to file to save logs to
    :type filename: str | None
    """
    # Use handler to redirect output
    handler: logging.Handler
    if filename:
        handler = logging.FileHandler(filename, encoding="utf-8")
    else:
        handler = logging.StreamHandler(sys.stdout)

    handler.formatter = logging.Formatter(
        "[%(asctime)s] %(levelname)s: %(message)s",
        datefmt="%Y-%m-%mT%H:%M:%S",
    )
    logging.basicConfig(level=level, handlers=[handler])


def setup_wandb(project: str, config: dict) -> None:
    """
    Initialize Weights & Biases logging.

    :param project: W&B project name to pass results to
    :type project: str
    :param config: Experimental setup to save in the W&B project
    :type config: dict
    """
    import wandb

    wandb.init(project=project, config=config)
    LOGGER.info(f"Weights & Biases logging initialized under {project!r} project.")


def terminate_wandb() -> None:
    """
    Terminate Weights & Biases logging.
    """
    import wandb

    wandb.finish()
    LOGGER.info("Weights & Biases logging terminated.")
