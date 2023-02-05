"""
Main driver code for whatever I decide to do

"""
from pprint import pprint
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
    plot.plot_counts(counts, dump["title"])

    plot.plot_reacts(read.count_reactions(dump))

    plot.plot_reacts(read.count_reactions(dump), total_counts=counts)

    # Get a dict of dicts of who reacted to who
    reacts = read.count_reactions(dump, return_strs=True)
    pprint(reacts)

    plt.show()


if __name__ == "__main__":
    main()
