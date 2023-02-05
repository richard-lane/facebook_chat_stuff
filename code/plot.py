"""
Utils for plotting stuff

"""
from typing import Tuple
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
    Plot grid of reactions

    """
