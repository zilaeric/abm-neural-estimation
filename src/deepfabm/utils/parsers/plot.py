from __future__ import annotations

from .base import Parser


class PlotParser(Parser):
    """Plotting functionality parser."""

    def _add_positional(self) -> None:
        self.positional.add_argument(
            dest="type",
            help="choose between plotting empirical and simulated data",
            type=str,
            choices=["emp", "sim"],
        )

    def _add_optional(self) -> None:
        self.optional.add_argument(
            "--data",
            "-d",
            dest="data",
            help="choose empirical data to estimate model for, else use simulated data",
            type=str,
            metavar="STR",
            default=None,
        )

        self.add_seed()
