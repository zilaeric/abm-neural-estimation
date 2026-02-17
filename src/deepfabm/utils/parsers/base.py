from __future__ import annotations

import logging
from abc import ABC
from argparse import ArgumentParser


class Parser(ABC):
    """Abstract base class for parsers."""

    def __init__(self):
        # Initialize parser
        self.parser = ArgumentParser(add_help=False)

        # Define argument groups
        self.positional = self.parser.add_argument_group("positional arguments")
        self.required = self.parser.add_argument_group("required arguments")
        self.optional = self.parser.add_argument_group("optional arguments")

        # Add parameters to parser group by group
        self._add_positional()
        self._add_required()
        self._add_optional()

        # Add help parameter to optional arguments
        self.optional.add_argument(
            "--help",
            "-h",
            help="show this help message and exit",
            action="help",
        )

    def add_verbose(self) -> None:
        self.optional.add_argument(
            "--verbose",
            "-v",
            dest="loglevel",
            help="set loglevel to DEBUG",
            action="store_const",
            default=logging.INFO,
            const=logging.DEBUG,
        )

    def add_seed(self) -> None:
        self.optional.add_argument(
            "--seed",
            "-s",
            dest="seed",
            help="reproducibility seed number",
            type=int,
            metavar="INT",
            default=42,
        )

    def _add_positional(self) -> None:
        """Add all specified parameters to the positional argument group."""
        pass

    def _add_required(self) -> None:
        """Add all specified parameters to the required argument group."""
        pass

    def _add_optional(self) -> None:
        """Add all specified parameters to the optional argument group."""
        pass
