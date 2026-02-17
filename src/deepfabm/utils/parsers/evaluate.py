from __future__ import annotations

from .base import Parser


class EvaluateParser(Parser):
    """Calibration model evaluation parser."""

    def _add_positional(self):
        self.positional.add_argument(
            dest="folder",
            help="choose results folder with trained weights to use for evaluation",
            type=str,
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
        self.add_verbose()
