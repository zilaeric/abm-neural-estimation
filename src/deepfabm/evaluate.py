from __future__ import annotations

from argparse import Namespace

from deepfabm.utils import LOGGER, initialize_run, terminate_run


def main(setup: Namespace) -> int:
    """
    Performs inference using neural network trained to calibrate parameters of
    a financial agent-based model.

    :param setup: Experimental setup
    :type setup: Namespace
    :return: Return value of the program
    :rtype: int
    """
    setup = initialize_run(setup)

    LOGGER.info("Initiating the evaluation process...")

    # TODO Load or generate dataset

    # TODO Assess model performance on dataset

    LOGGER.info("Finished the evaluation process!")

    terminate_run(setup)

    return 0
