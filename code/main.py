"""
Main driver code for whatever I decide to do

"""
import streamlit as st
import matplotlib.pyplot as plt
from pprint import pformat

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
    count_plot,_ = plot.plot_counts(counts, dump["title"])

    react_plot, _ = plot.plot_reacts(read.count_reactions(dump))

    scaled_reacts, _ = plot.plot_reacts(read.count_reactions(dump), total_counts=counts)

    # Get a dict of dicts of who reacted to who
    reacts = read.count_reactions(dump, return_strs=True)

    # Streamlit
    st.title("The Shakira Respecters")
    st.write("Who talks the most:")
    st.write(count_plot)

    st.write("Who reacts to who:")
    st.write(react_plot)
    st.write("i am the king of reacts")

    st.write("Scaled by overall counts:")
    st.write(scaled_reacts)
    st.write("turns out its really holly")

    st.write("what reactions does everyone use")
    st.write("I got bored here so it isnt nicely formatted")
    st.write(pformat(reacts))


if __name__ == "__main__":
    main()
