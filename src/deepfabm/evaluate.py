import sys

from deepfabm import __version__

from deepfabm.environments import load_environment

from deepfabm.policies import load_policy

from deepfabm.utils import EvaluateParser
from deepfabm.utils import LOGGER, setup_logging, setup_wandb, terminate_wandb
from deepfabm.utils import set_seed

__author__ = "Eric Zila"
__copyright__ = "Eric Zila"
__license__ = "MIT"


def main(args):
    """
    Performs model evaluation.

    Args:
        args: The command-line arguments passed to the script.

    Returns:
        None
    """
    # Parse the command-line arguments
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
    
    # Load environment
    env = load_environment(args.environment)

    # Select policy
    policy = load_policy(args.policy, env)

    # TODO Load model and weights if trained policy is selected
    if args.policy == "trained":
        raise NotImplementedError()

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
