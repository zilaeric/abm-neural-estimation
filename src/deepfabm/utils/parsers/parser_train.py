from __future__ import annotations

from .parser_base import Parser


class TrainParser(Parser):
    """Calibration model training parser."""

    def _add_positional(self) -> None:
        self.positional.add_argument(
            dest="experiment",
            help="path to experiment configuration in the '/experiments' folder",
            type=str,
        )

    def _add_optional(self) -> None:
        self.add_seed()
        self.add_verbose()

        self.optional.add_argument(
            "--wandb",
            "-wb",
            dest="wandb",
            help="Weights & Biases project name; do not use W&B if not set",
            type=str,
            metavar="STR",
            default=None,
        )
