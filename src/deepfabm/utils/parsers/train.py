from __future__ import annotations

from .base import Parser


class TrainParser(Parser):
    """Calibration model training parser."""

    def _add_positional(self) -> None:
        self.positional.add_argument(
            dest="experiment",
            help="choose experiment configuration from the 'experiments' folder",
            type=str,
        )

    def _add_optional(self) -> None:
        self.add_seed()
        self.add_verbose()

        self.optional.add_argument(
            "--wandb",
            "-wb",
            dest="wandb",
            help="set Weights & Biases project name to store experiment run to",
            type=str,
            metavar="STR",
            default=None,
        )
