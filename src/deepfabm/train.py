from __future__ import annotations

from argparse import Namespace

from deepfabm.utils import LOGGER, initialize_run, terminate_run


def main(setup: Namespace) -> int:
    """
    Trains neural network to calibrate parameters of a financial agent-based model.

    :param setup: Experimental setup
    :type setup: Namespace
    :return: Return value of the program
    :rtype: int
    """
    setup = initialize_run(setup)

    LOGGER.info("Initiating the training process...")

    # TODO Initialize financial agent-based model

    # TODO Initialize calibration model

    # TODO Train calibration model using financial agent-based model

    # TODO Save trained calibration model

    LOGGER.info("Finished the training process!")

    terminate_run(setup)

    return 0
