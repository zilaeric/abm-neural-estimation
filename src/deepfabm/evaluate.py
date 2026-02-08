import sys

from deepfabm.utils import EvaluateParser
from deepfabm.utils import LOGGER, setup_logging, setup_wandb, terminate_wandb
from deepfabm.utils import set_seed


def main(args):
    """
    Performs model evaluation.

    Args:
        args: CLI arguments passed to the script

    Returns:
        None
    """
    # Parse the CLI arguments
    parser = EvaluateParser()
    args = parser.parse_args(args)

    # Set up standard output logging
    setup_logging(args.loglevel)
    LOGGER.info(f"Dictionary of parsed arguments: {vars(args)}")

    # Set up Weights & Biases logging
    if args.wandb:
        setup_wandb(project=args.wandb_project, config=vars(args))

    # Set up the random seed
    set_seed(args.seed)

    LOGGER.info("Initiating the evaluation process...")

    # TODO Assess model performance on environment

    LOGGER.info("Finished the evaluation process!")

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
