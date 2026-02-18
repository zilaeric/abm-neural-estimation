from __future__ import annotations

import os

import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
import numpy as np

_PLOT_CONTEXT = {
    "figure.figsize": (3.5, 2.0),
    "figure.dpi": 300,
    "savefig.dpi": 300,
    "font.family": "serif",
    "font.serif": [
        "Computer Modern Roman",
        "CMU Serif",
        "Latin Modern Roman",
        "DejaVu Serif",
    ],
    "mathtext.fontset": "cm",
    "font.size": 8,
    "axes.labelsize": 8,
    "xtick.labelsize": 7,
    "ytick.labelsize": 7,
    "axes.linewidth": 0.6,
    "grid.linewidth": 0.5,
    "lines.linewidth": 0.9,
    "pdf.fonttype": 42,
    "ps.fonttype": 42,
}


def plot_returns(returns: list[float], folder: str, dates: list[str] = None) -> None:
    """
    Plot returns while maintaining readability in two-column PDF document.

    :param returns: Time-series values
    :type returns: list[float]
    :param folder: Folder within the "/plots" folder to use when saving the plot
    :type folder: str
    :param dates: For empirical time-series, dates corresponding to observations
    :type dates: list[str]
    """
    # Final plot destination
    path = os.path.join("plots", folder, "returns.pdf")
    os.makedirs(os.path.dirname(path), exist_ok=True)

    # Use shared plot context
    with plt.rc_context(_PLOT_CONTEXT):
        fig, ax = plt.subplots(constrained_layout=True)

        # Prepare x-axis values
        x = (
            np.arange(len(returns))
            if dates is None
            else np.asarray(dates, dtype="datetime64")
        )

        # Plot series
        ax.plot(x, returns, color="black")

        # Set axis labels
        ax.set_xlabel("time")
        ax.set_ylabel("returns (%)")

        # Add grid
        ax.grid(True, which="major", axis="both", color="lightgrey")

        # Remove x-axis margins
        ax.margins(x=0)

        # Format y-axis as percentage points
        ax.yaxis.set_major_formatter(
            mticker.FuncFormatter(lambda y, _pos: f"{100.0 * y:g}")
        )

        # Center y-axis around 0
        y_lim = 1.05 * float(np.max(np.abs(returns)))
        ax.set_ylim(-y_lim, y_lim)

        # Save figure
        fig.savefig(path, format="pdf")
