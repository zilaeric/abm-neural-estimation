import sys

from deepfabm.utils import initialize_run, terminate_run
from deepfabm.utils import LOGGER


def main(args):
    """
    Performs inference using neural network trained to calibrate parameters of a 
    financial agent-based model.
    
    :param args: CLI arguments passed during invocation
    """
    initialize_run("evaluate", args)

    LOGGER.info("Initiating the evaluation process...")

    # TODO Assess model performance on environment

    LOGGER.info("Finished the evaluation process!")

    terminate_run(args)

def run():
    """
    Calls the main function when CLI is used.
    """
    main(sys.argv[1:])


if __name__ == "__main__":
    run()
