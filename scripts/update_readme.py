from __future__ import annotations

import argparse
import os
import re
import subprocess

BLOCKS: dict[str, list[str]] = {
    "train": ["deepfabm", "train", "--help"],
    "evaluate": ["deepfabm", "evaluate", "--help"],
    "plot-emp": ["deepfabm", "plot", "emp", "--help"],
    "plot-sim": ["deepfabm", "plot", "sim", "--help"],
}


def _run_help(command: list[str]) -> str:
    """
    Run `command` and return its output.

    :param command: Command arguments split into a list
    :type command: list[str]
    :return: Standard output of the command
    :rtype: str
    """
    # Prepare execution envionment
    env = {
        **os.environ,
        "LC_ALL": "C",
        "LANG": "C",
        "COLUMNS": "200",  # Line length
    }

    # Execute command
    proc = subprocess.run(command, text=True, capture_output=True, check=False, env=env)

    if proc.returncode != 0:
        raise RuntimeError("Command execution failed!")

    return proc.stdout


def _render_block(command: list[str], help: str) -> str:
    """
    Render final code block to add to documentation.

    :param command: Command arguments split into a list
    :type command: list[str]
    :param help: Output of the command
    :type help: str
    :return: Rendered command block combining command and its output
    :rtype: str
    """
    return "```\n" + "$ " + " ".join(command) + "\n" + help + "```"


def _replace_block(readme: str, key: str, block: str) -> str:
    """
    Replace old code block in documentation with new code block.

    :param readme: Original documentation
    :type readme: str
    :param key: Key used to identify of code block
    :type key: str
    :param block: New code block to insert into documentation
    :type block: str
    :return: Documentation with replaced code block
    :rtype: str
    """
    # Identify marks in documentation for code replacement
    start = f"<!-- CLI:{key}:START -->"
    end = f"<!-- CLI:{key}:END -->"

    # Match code in documentation between marks
    pattern = re.compile(rf"(?s)({re.escape(start)}\n)(.*?)(\n{re.escape(end)})")
    match = pattern.search(readme)
    block = match.group(1) + block + match.group(3)

    return pattern.sub(block, readme, count=1)


def main() -> int:
    # Create parser to enable checking for changes in pre-commit hook
    parser = argparse.ArgumentParser(
        description="Auto-update CLI usage blocks in documentation.",
    )
    parser.add_argument(
        "--check",
        action="store_true",
        help="avoid making changes, return non-zero if README.md would change",
    )
    args = parser.parse_args()

    # Open and read README.md
    with open("README.md", "r") as f:
        readme_original = f.read()

    # Copy original to recognize changed content
    readme_updated = readme_original

    for key in BLOCKS:
        help = _run_help(BLOCKS[key])
        block = _render_block(BLOCKS[key], help)
        readme_updated = _replace_block(readme_updated, key, block)

    if readme_updated == readme_original:
        return 0

    if args.check:
        return 1

    # Write updates to README.md
    with open("README.md", "w") as f:
        f.write(readme_updated)

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
