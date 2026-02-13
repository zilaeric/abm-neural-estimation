from __future__ import annotations

import sys
from argparse import Namespace

from deepfabm.utils import LOGGER, initialize_run, terminate_run


def main(args: list[str] | Namespace) -> int:
    """
    Performs inference using neural network trained to calibrate parameters of
    a financial agent-based model.

    :param args: CLI arguments passed during invocation
    :type args: list[str] | argparse.Namespace
    :return: Return value of the program
    :rtype: int
    """
    args = initialize_run("evaluate", args)

    LOGGER.info("Initiating the evaluation process...")

    # TODO Assess model performance on environment

    LOGGER.info("Finished the evaluation process!")

    terminate_run(args)

    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
