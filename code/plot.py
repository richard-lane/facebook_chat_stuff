"""
Utils for plotting stuff

"""
import matplotlib.pyplot as plt


def plot_counts(data: dict, title: str, ylabel: str) -> None:
    """
    Plot dict data={label:count} as a bar chart

    """
    plt.bar(data.keys(), data.values())

    plt.ylabel(ylabel)
    plt.xticks(rotation=90)

    plt.title(title)
    plt.show()
