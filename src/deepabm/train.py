import sys

from deepabm import __version__
from deepabm.utils import TrainParser
from deepabm.utils import LOGGER, setup_logging, setup_wandb, terminate_wandb
from deepabm.utils import set_seed

__author__ = "Eric Zila"
__copyright__ = "Eric Zila"
__license__ = "MIT"


def main(args):
    """
    Performs model training.

    Args:
        args: The command-line arguments passed to the script.

    Returns:
        None
    """
    # Parse the command-line arguments
    parser = TrainParser()
    args = parser.parse_args(args)

    # Set up logging
    setup_logging(args.loglevel)
    LOGGER.info(f"Dictionary of parsed arguments: {vars(args)}")

    # Set up Weights & Biases logging
    if args.wandb:
        setup_wandb(project=args.wandb_project, config=vars(args))

    # Set up the random seed
    set_seed(args.seed)

    LOGGER.info("Initiating the training process...")
    
    # TODO Load dataset

    # TODO Select model

    # TODO Train model on dataset

    # TODO Save trained model

    LOGGER.info("Finished the training process!")

    # Terminate Weights & Biases logging
    if args.wandb:
        terminate_wandb()


def run():
    """
    Calls the main function when CLI is used.
    """
    main(sys.argv[1:])


if __name__ == "__main__":
    run()
