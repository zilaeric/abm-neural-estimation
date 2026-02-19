from __future__ import annotations

import sys
from argparse import Namespace

from deepfabm.models import load_model
from deepfabm.utils import load_data, plot_returns, set_seed


def main(setup: Namespace) -> int:
    """
    Plots simulated and empirical data.

    To plot simulated data, model identifier, parametrization, number of observations,
    and length of the burn-in period must be specified. To plot empirical data, path to
    the dataset must be specified.

    All plots are saved to the '/plots' folder with the model name used as the filename
    for simulated data and the dataset name used as the filename for empirical data.

    :param setup: CLI arguments passed during invocation
    :type setup: Namespace
    :return: Return value of the program
    :rtype: int
    """
    # Plot empirical data
    if setup.type == "emp":
        # Load empirical data
        data = load_data(setup.data)

        # Plot series
        plot_returns(data["returns"], folder=setup.data[:-4], dates=data["dates"])

    # Plot simulated data
    if setup.type == "sim":
        # Set random seed
        set_seed(setup.seed)

        # Load simulation model and generate data
        model = load_model(setup.model)
        parameters = model.get_parameters(setup.parametrization)
        data = model.generate(parameters, setup.obs, setup.burn, 1)

        # Plot series
        plot_returns(data[0].tolist(), folder=setup.model)

    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
