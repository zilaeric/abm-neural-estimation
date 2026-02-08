import sys

from deepfabm.utils import initialize_run, terminate_run
from deepfabm.utils import LOGGER


def main(args):
    """
    Trains neural network to calibrate parameters of a financial agent-based model.
    
    :param args: CLI arguments passed during invocation
    """
    initialize_run("train", args)

    LOGGER.info("Initiating the training process...")
    
    # TODO Load dataset

    # TODO Select model

    # TODO Train model on dataset

    # TODO Save trained model

    LOGGER.info("Finished the training process!")

    terminate_run(args)


def run():
    """
    Calls the main function when CLI is used.
    """
    main(sys.argv[1:])


if __name__ == "__main__":
    run()
