"""
Utils for reading message info from the JSON dump

"""
import json


def read_dump(json_path: str) -> dict:
    """
    Read stuff from a JSON file

    """
    with open(json_path, "r") as f:
        return json.load(f)


def count_messages(data: dict) -> dict:
    """
    Take a dump of JSON data, count how many messages each sender sent

    Returns dict {sender:count}

    """
    # Create a dict of participant:message count
    message_counts = {d["name"]: 0 for d in data["participants"]}

    # Iterate over every message finding who sent it and incrementing each counter
    for message in data["messages"]:
        sender = message["sender_name"]
        try:
            message_counts[sender] += 1
        except KeyError:
            # Message sent by someone who is no longer a participant
            message_counts.update({sender: 1})

    return message_counts


def count_reactions(data: dict) -> dict:
    """
    Take a dump of JSON data, count how many messages each participant reacted to

    Returns dict {reacter:count}

    """
    # Create a dict of participant:message count
    react_counts = {d["name"]: 0 for d in data["participants"]}

    # Iterate over every message finding who reacted to it and incrementing each counter
    for message in data["messages"]:
        try:
            reactions = message["reactions"]
            for reaction in reactions:
                reacter = reaction["actor"]
                try:
                    react_counts[reacter] += 1
                except KeyError:
                    # Reacter has left the group
                    react_counts.update({reacter: 1})
        except KeyError:
            # Message has no reactions
            pass

    return react_counts
    # data_dump = read_message_data(frog_data_file)

    # message_counts = count_messages(data_dump)
    # print(message_counts)
    # plot_counts(message_counts, data_dump["title"], "Message Counts")

    # react_counts = count_reactions(data_dump)
    # plot_counts(react_counts, data_dump["title"], "React Counts")
