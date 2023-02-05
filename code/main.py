"""
Main driver code for whatever I decide to do

"""
import matplotlib.pyplot as plt

# My stuff
import read
import plot


def main():
    """
    Print everything

    """
    # This is the path to our JSON message dump
    path = "./data/messages/inbox/theshakirarespecters_5703385153039362/message_1.json"

    dump = read.read_dump(path)

    counts = read.count_messages(dump)

    fig, _ = plot.plot_counts(counts, dump["title"])
    fig.tight_layout()

    plt.show()


if __name__ == "__main__":
    main()
