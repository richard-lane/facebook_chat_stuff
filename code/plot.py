"""
Utils for plotting stuff

"""
from typing import Tuple
import numpy as np
import matplotlib.pyplot as plt


def plot_counts(data: dict, title: str) -> Tuple[plt.Figure, plt.Axes]:
    """
    Plot dict data={label:count} as a bar chart

    """
    fig, axis = plt.subplots()

    axis.bar(data.keys(), data.values())

    axis.set_ylabel("Message Count")
    axis.set_xticks(axis.get_xticks(), rotation=90)

    axis.set_title(title)

    return fig, axis


def plot_reacts(
    react_counts: dict, *, total_counts: dict = None
) -> Tuple[plt.Figure, plt.Axes]:
    """
    Plot a grid of reactions

    :param react_counts: dict of dicts {reactor: {reactee: count}}
    :param total_counts: dict of {reactor: total messages}: used to optionally scale counts.

    :returns: Figure
    :returns: Axes

    """
    # Get a list of lists of counts
    reacts = [[] for _ in react_counts]
    for i, counts in enumerate(react_counts.values()):
        for count in counts.values():
            reacts[i].append(count)

    if total_counts is not None:
        totals = list(total_counts.values())
        for i, _ in enumerate(total_counts):
            for j, _ in enumerate(total_counts):
                reacts[i][j] = reacts[i][j] / totals[j]

    # Plot the matrix of counts
    fig, axis = plt.subplots()
    axis.matshow(reacts)

    # Show the raw numbers only if we aren't scaling
    for (i, j), z in np.ndenumerate(reacts):
        axis.text(j, i, f"{z:.3f}", ha="center", va="center")

    # X axis below
    axis.tick_params(axis="x", top=True)

    # labels
    names = list(react_counts)
    axis.set_xticks(
        range(len(react_counts)),
        labels=names,
        rotation=90,
    )
    axis.set_yticks(range(len(react_counts)), labels=names)

    fig.supxlabel("Reactee")
    fig.supylabel("Reactor")

    if total_counts is None:
        fig.suptitle("Reacts")
    else:
        fig.suptitle("Reacts per message")

    fig.tight_layout()

    return fig, axis
