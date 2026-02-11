import sys

from deepfabm.utils import LOGGER, initialize_run, terminate_run


def main(args: list[str]) -> int:
    """
    Performs inference using neural network trained to calibrate parameters of
    a financial agent-based model.
    
    :param args: CLI arguments passed during invocation
    :type args: list[str]
    """
    args = initialize_run("evaluate", args)

    LOGGER.info("Initiating the evaluation process...")

    # TODO Assess model performance on environment

    LOGGER.info("Finished the evaluation process!")

    terminate_run(args)

    return 0


def run(argv: list[str] | None = None) -> int:
    """
    Calls the main function when CLI is used.
    """
    return main(sys.argv[1:] if argv is None else argv)


if __name__ == "__main__":
    raise SystemExit(run())
