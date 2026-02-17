from __future__ import annotations

from .base import Parser


class EvaluateParser(Parser):
    """Calibration model evaluation parser."""

    def _add_positional(self):
        self.positional.add_argument(
            dest="folder",
            help="path to results folder with trained weights in the '/results' folder",
            type=str,
        )

    def _add_optional(self) -> None:
        self.optional.add_argument(
            "--data",
            "-d",
            dest="data",
            help="path to empirical data in the '/data' folder, else simulate data",
            type=str,
            metavar="STR",
            default=None,
        )

        self.add_seed()
        self.add_verbose()
