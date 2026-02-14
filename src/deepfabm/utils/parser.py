from __future__ import annotations

import argparse
import logging


class BaseParser:
    def __init__(self, description="Parser template", include_common: bool = True):
        # Initialize parser
        self.parser = argparse.ArgumentParser(description=description, add_help=False)

        # Define argument groups
        self.required = self.parser.add_argument_group("required arguments")
        self.optional = self.parser.add_argument_group("optional arguments")

        self.optional.add_argument(
            "--help",
            "-h",
            help="show this help message and exit",
            action="help",
        )

        # Include shared optional arguments
        if include_common:
            self.optional.add_argument(
                "--verbose",
                "-v",
                dest="loglevel",
                help="set loglevel to DEBUG",
                action="store_const",
                default=logging.INFO,
                const=logging.DEBUG,
            )

            self.optional.add_argument(
                "--seed",
                "-s",
                dest="seed",
                help="set seed for reproducibility",
                type=int,
                metavar="INT",
                default=42,
            )

            self.optional.add_argument(
                "--wandb",
                "-wb",
                dest="wandb",
                help="set Weights & Biases project name to store experiment run to",
                type=str,
                metavar="STR",
                default=None,
            )

    def parse_args(self, args) -> dict:
        return vars(self.parser.parse_args(args))


class TrainParser(BaseParser):
    """Calibration model training parser."""

    def __init__(self):
        super().__init__()

        # Add required and optional parameters to parser
        self.add_required()
        self.add_optional()

    def add_required(self):
        self.required.add_argument(
            "--architecture",
            "-a",
            dest="architecture",
            help="choose network architecture to train",
            type=str,
            choices=["gru"],
            required=True,
        )

    def add_optional(self):
        pass


class EvaluateParser(BaseParser):
    """Calibration model evaluation parser."""

    def __init__(self):
        super().__init__()

        # Add required and optional parameters to parser
        self.add_required()
        self.add_optional()

    def add_required(self):
        self.required.add_argument(
            "--folder",
            "-f",
            dest="folder",
            help="choose results folder with trained weights to use for evaluation",
            type=str,
            metavar="STR",
            required=True,
        )

    def add_optional(self):
        self.optional.add_argument(
            "--data",
            "-d",
            dest="data",
            help="choose empirical data to estimate model for, else use simulate data",
            type=str,
            metavar="STR",
            default=None,
        )


class CLIParser(BaseParser):
    """Command-line interface parser."""

    def __init__(self):
        super().__init__(
            description=("DeepFABM command-line interface. Choose from methods below."),
            include_common=False,
        )

        subparsers = self.parser.add_subparsers(
            dest="command",
            required=True,
        )

        subparsers.add_parser(
            "train",
            help="calibration model training",
            description="DeepFABM model training interface.",
            add_help=False,
            parents=[TrainParser().parser],
        )

        subparsers.add_parser(
            "evaluate",
            help="calibration model evaluation",
            description="DeepFABM model evaluation interface.",
            add_help=False,
            parents=[EvaluateParser().parser],
        )
