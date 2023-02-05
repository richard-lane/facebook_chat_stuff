"""
Utils for reading message info from the JSON dump

"""
import os
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


def main():
    wap_data_file = "../messages/inbox/starseedsforwaps_ngoe_w6-eq/message_1.json"
    frog_data_file = (
        "../messages/archived_threads/forbiddenfroggy_yjdoqdemew/message_1.json"
    )
    data_dump = read_message_data(frog_data_file)

    message_counts = count_messages(data_dump)
    print(message_counts)
    plot_counts(message_counts, data_dump["title"], "Message Counts")

    react_counts = count_reactions(data_dump)
    plot_counts(react_counts, data_dump["title"], "React Counts")

    # reacts_per_message = dict()
    # for participant in data_dump["participants"]:
    #    name = participant["name"]
    #    reacts_per_message.update({name: react_counts[name] / message_counts[name]})
    # plot_counts(reacts_per_message, data_dump["title"], "Reacts per Message")


if __name__ == "__main__":
    main()
