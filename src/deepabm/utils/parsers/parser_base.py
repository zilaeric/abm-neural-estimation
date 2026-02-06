import yaml
import logging

from argparse import ArgumentParser


class BaseParser:
    def __init__(self, description="Base parser"):
        # Initialize parser
        self.parser = ArgumentParser(description=description, add_help=False)

        # Define argument groups
        self.required = self.parser.add_argument_group('Required arguments')
        self.command = self.parser.add_argument_group('Command-specific optional arguments')
        self.common = self.parser.add_argument_group('Common optional arguments')

        self.common.add_argument(
            "--help",
            "-h",
            help="show this help message and exit",
            action="help",
        )

        self.common.add_argument(
            "--verbose",
            "-v",
            dest="loglevel",
            help="set loglevel to INFO",
            action="store_const",
            const=logging.INFO,
        )

        self.common.add_argument(
            "--wandb",
            "-wb",
            dest="wandb",
            help="enable Weights & Biases logging",
            action="store_true",
            default=False,
        )

        self.common.add_argument(
            "--wandb_project",
            "-wbp",
            dest="wandb_project",
            help="set Weights & Biases project",
            type=str,
            metavar="STR",
            default="deepabm",
        )

        self.common.add_argument(
            "--seed",
            "-s",
            dest="seed",
            help="set seed for reproducibility",
            type=int,
            metavar="INT",
            default=42,
        )

    def parse_args(self, args):
        return self.parser.parse_args(args)
    
    def read_yaml(self, source):
        with open(source, 'r') as file:
            data = yaml.safe_load(file)
        
        return data
