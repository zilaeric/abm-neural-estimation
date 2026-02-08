import sys
import logging
import wandb

LOGGER = logging.getLogger(__name__)


def setup_logging(loglevel):
	"""
	Set up logging configuration.

	Args:
		loglevel (int): The log level to be set.

	Returns:
		None
	"""
	logformat = "[%(asctime)s] %(levelname)s: %(message)s"
	logging.basicConfig(
		level=loglevel, stream=sys.stdout, format=logformat, datefmt="%Y-%m-%d %H:%M:%S"
	)


def setup_wandb(project="deepabm", config=None):
	"""
	Initiate Weights & Biases logging.

	Returns:
		None
	"""
	wandb.init(project=project, config=config)
	LOGGER.info(f"Weights & Biases logging initialized under '{project}' project.")


def terminate_wandb():
	"""
	Terminate Weights & Biases logging.

	Returns:
		None
	"""
	wandb.finish()
	LOGGER.info("Weights & Biases logging terminated.")
