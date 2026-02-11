import argparse
import logging


class BaseParser:
    def __init__(self, description="Parser template"):
        # Initialize parser
        self.parser = argparse.ArgumentParser(description=description, add_help=False)

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

    def parse_args(self, args) -> argparse.Namespace:
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
            help="choose results folder with trained weights to use for evaluation",
            type=str,
            metavar="STR",
            required=True,
        )

        self.optional.add_argument(
            "--data",
            "-d",
            dest="data",
            help="choose empirical data to estimate model for, else use simulate data",
            type=str,
            metavar="STR",
            default=None,
        )
