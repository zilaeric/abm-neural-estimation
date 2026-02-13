from __future__ import annotations

import sys
from argparse import Namespace

from deepfabm.utils import LOGGER, initialize_run, terminate_run


def main(args: list[str] | Namespace) -> int:
    """
    Trains neural network to calibrate parameters of a financial agent-based model.

    :param args: CLI arguments passed during invocation
    :type args: list[str] | argparse.Namespace
    :return: Return value of the program
    :rtype: int
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


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
