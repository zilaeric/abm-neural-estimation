from __future__ import annotations

import csv
import os


def load_data(file: str) -> dict[str, list]:
    """
    Load data from the selected CSV file from the "/data" folder.

    It is expected that the CSV file contains four columns - `date`, `price`,
    `price_ln`, and `return`. The `date` column should be in the `YYYY-MM-DD` format.

    :param file: Name of the data file
    :type file: str
    :return: Dictionary with column names from the data file as keys
    :rtype: dict[str, list]
    """
    # Determine full relative path to the data file
    path = os.path.join("data", file)

    # Initialize lists for columns
    dates: list[str] = []
    prices: list[float] = []
    prices_ln: list[float] = []
    returns: list[float] = []

    # Iterate through the data file
    with open(path) as f:
        reader = csv.DictReader(f)
        for row in reader:
            dates.append(str(row["date"]))
            prices.append(float(row["price"]))
            prices_ln.append(float(row["price_ln"]))
            returns.append(float(row["return"]))

    return {
        "dates": dates,
        "prices": prices,
        "prices_ln": prices_ln,
        "returns": returns,
    }
