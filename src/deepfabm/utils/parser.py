from __future__ import annotations

from argparse import ArgumentParser, Namespace

from .parsers import EvaluateParser, TrainParser


class CLIParser:
    """Command-line interface parser."""

    def __init__(self):
        # Initialize parser
        description = "DeepFABM command-line interface. Choose from methods below."
        self.parser = ArgumentParser(description=description, add_help=False)

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

        self.optional = self.parser.add_argument_group("optional arguments")
        self.optional.add_argument(
            "--help",
            "-h",
            help="show this help message and exit",
            action="help",
        )

    def parse_args(self, args: list[str]) -> Namespace:
        """
        Parses arguments into dictonary.

        :param args: List of arguments and values, typically retrieved as CLI arguments
        :type args: list[str]
        :return: Namespace mapping argument names to their values
        :rtype: Namespace
        """
        return self.parser.parse_args(args)
