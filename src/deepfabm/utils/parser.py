import logging

from argparse import ArgumentParser


class BaseParser:
    def __init__(self, description="Parser template"):
        # Initialize parser
        self.parser = ArgumentParser(description=description, add_help=False)

        # Define argument groups
        self.required = self.parser.add_argument_group("Required arguments")
        self.optional = self.parser.add_argument_group("Optional arguments")

        self.optional.add_argument(
            "--help",
            "-h",
            help="show this help message and exit",
            action="help",
        )

        self.optional.add_argument(
            "--verbose",
            "-v",
            dest="loglevel",
            help="set loglevel to INFO",
            action="store_const",
            const=logging.INFO,
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
            help="set Weights & Biases project to store training run progress",
            type=str,
            metavar="STR",
            default=None,
        )

    def parse_args(self, args):
        return self.parser.parse_args(args)


class TrainParser(BaseParser):
    def __init__(self):
        super().__init__(description="Parser for training")

        self.required.add_argument(
            "--architecture",
            "-a",
            dest="architecture",
            help="choose network architecture to train",
            type=str,
            choices=["gru"],
            required=True,
        )


class EvaluateParser(BaseParser):
    def __init__(self):
        super().__init__(description="Parser for evaluation")

        self.required.add_argument(
            "--folder",
            "-f",
            dest="folder",
            help="choose results folder containing trained network weights to use for evaluation",
            type=str,
            metavar="STR",
            required=True,
        )

        self.optional.add_argument(
            "--data",
            "-d",
            dest="data",
            help="choose empirical dataset to estimate model for, otherwise use simulated dataset",
            type=str,
            metavar="STR",
            default=None,
        )
