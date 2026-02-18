from __future__ import annotations

import sys
from argparse import Namespace

from deepfabm.models import load_model
from deepfabm.utils import load_data, plot_returns, set_seed


def main(args: list[str] | Namespace) -> int:
    """
    Plots simulated and empirical data.

    To plot simulated data, model identifier, number of observations, and length of the
    burn-in period must be specified. To plot empirical data, path to the dataset must
    be specified.

    All plots are saved to the '/plots' folder with the model name used as the filename
    for simulated data and the dataset name used as the filename for empirical data.

    :param args: CLI arguments passed during invocation
    :type args: list[str] | argparse.Namespace
    :return: Return value of the program
    :rtype: int
    """
    # Plot empirical data
    if args.type == "emp":
        # Load empirical data
        data = load_data(args.data)

        # Plot series
        plot_returns(data["returns"], folder=args.data[:-4], dates=data["dates"])

    # Plot simulated data
    if args.type == "sim":
        # Set random seed
        set_seed(args.seed)

        # Load simulation model and generate data
        model = load_model(args.model)
        parameters = model.get_parameters(args.parametrization)
        data = model.generate(parameters, args.obs, args.burn, 1)

        # Plot series
        plot_returns(data[0].tolist(), folder=args.model)

    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
