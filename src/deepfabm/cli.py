from __future__ import annotations

import sys

from deepfabm.evaluate import main as evaluate_main
from deepfabm.train import main as train_main
from deepfabm.utils.parser import CLIParser


def main(args: list[str]) -> int:
    """
    Triggers requested sub-command.

    :param args: CLI arguments passed during invocation
    :type args: list[str]
    :return: Return value of the program
    :rtype: int
    """
    parsed = CLIParser().parse_args(args)

    if parsed.command == "train":
        return train_main(parsed)
    if parsed.command == "evaluate":
        return evaluate_main(parsed)

    # Throw error if unknown command is used
    raise ValueError(f"Unknown command: {parsed.command!r}")


def run(argv: list[str] | None = None) -> int:
    """
    Entry point for command-line interface (CLI).

    :param argv: CLI arguments passed during invocation
    :type argv: list[str] | None
    :return: Return value of the program
    :rtype: int
    """
    return main(sys.argv[1:] if argv is None else argv)


if __name__ == "__main__":
    raise SystemExit(run())
