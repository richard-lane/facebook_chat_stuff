"""
Main driver code for whatever I decide to do

"""
import read


def main():
    """
    Print everything

    """
    # This is the path to our JSON message dump
    path = "./data/messages/inbox/theshakirarespecters_5703385153039362/message_1.json"

    dump = read.read_dump(path)


if __name__ == "__main__":
    main()
