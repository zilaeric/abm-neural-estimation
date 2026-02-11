import sys

from deepfabm.utils import LOGGER, initialize_run, terminate_run


def main(args: list[str]) -> int:
    """
    Trains neural network to calibrate parameters of a financial agent-based model.
    
    :param args: CLI arguments passed during invocation
    :type args: list[str]
    """
    args = initialize_run("train", args)

    LOGGER.info("Initiating the training process...")
    
    # TODO Load dataset

    # TODO Select model

    # TODO Train model on dataset

    # TODO Save trained model

    LOGGER.info("Finished the training process!")

    terminate_run(args)

    return 0


def run(argv: list[str] | None = None) -> int:
    """
    Calls the main function when CLI is used.
    """
    return main(sys.argv[1:] if argv is None else argv)


if __name__ == "__main__":
    raise SystemExit(run())
