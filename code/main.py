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
    plot.plot_counts(counts, dump["title"])

    plot.plot_reacts(read.count_reactions(dump))

    plot.plot_reacts(read.count_reactions(dump), total_counts=counts)
    plt.show()


if __name__ == "__main__":
    main()
