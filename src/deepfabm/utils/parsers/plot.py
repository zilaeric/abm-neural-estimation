from __future__ import annotations

from .base import Parser


class EmpiricalPlotParser(Parser):
    """Empirical data plotting parser."""

    def _add_required(self) -> None:
        self.required.add_argument(
            "--data",
            "-d",
            dest="data",
            help="path to empirical data in the '/data' folder",
            type=str,
            metavar="STR",
            required=True,
        )


class SimulatedPlotParser(Parser):
    """Simulated data plotting parser."""

    def _add_required(self) -> None:
        self.required.add_argument(
            "--model",
            "-m",
            dest="model",
            help="simulation model identifier",
            type=str,
            metavar="STR",
            required=True,
        )

        self.required.add_argument(
            "--obs",
            dest="obs",
            help="number of observations",
            type=int,
            metavar="INT",
            required=True,
        )

        self.required.add_argument(
            "--burn",
            dest="burn",
            help="burn-in period length",
            type=int,
            metavar="INT",
            required=True,
        )

    def _add_optional(self) -> None:
        self.add_seed()


class PlotParser(Parser):
    """Plotting functionality parser."""

    def _add_positional(self) -> None:
        subparsers = self.parser.add_subparsers(
            dest="type",
            required=True,
        )

        subparsers.add_parser(
            "emp",
            help="empirical data plotting",
            description="DeepFABM empirical data plotting interface.",
            add_help=False,
            parents=[EmpiricalPlotParser().parser],
        )

        subparsers.add_parser(
            "sim",
            help="simulated data plotting",
            description="DeepFABM simulated data plotting interface.",
            add_help=False,
            parents=[SimulatedPlotParser().parser],
        )
