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


def plot_reacts(react_counts: dict) -> Tuple[plt.Figure, plt.Axes]:
    """
    Plot a grid of reactions

    """
    print(react_counts)
    # Get a list of lists of counts
    reacts = [[] for _ in react_counts]
    for i, counts in enumerate(react_counts.values()):
        for count in counts.values():
            reacts[i].append(count)

    # Plot the grid
    fig, axis = plt.subplots()
    axis.matshow(reacts)

    # Show the numbers
    for (i, j), z in np.ndenumerate(reacts):
        axis.text(j, i, f"{z:.0f}", ha="center", va="center")

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

    fig.tight_layout()

    return fig, axis
