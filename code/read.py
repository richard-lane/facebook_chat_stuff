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


def count_reactions(data: dict, *, return_strs: bool = False) -> dict:
    """
    Take a dump of JSON data, count how many messages each participant reacted to

    Returns dict {reacter: {reactee: count}}

    """
    # Create a dict of participant:message count
    participants = tuple(person["name"] for person in data["participants"])

    # Dict of dicts if we're not returning strs
    # If we are returning strs, dict of dict of dicts
    react_counts = {
        d: {n: {} if return_strs else 0 for n in participants} for d in participants
    }

    # Iterate over every message finding who reacted to it and incrementing each counter
    for message in data["messages"]:
        try:
            reactions = message["reactions"]
            reactee = message["sender_name"]
            for reaction in reactions:
                reactor = reaction["actor"]
                try:
                    if return_strs:
                        react_str = reaction["reaction"]
                        try:
                            react_counts[reactor][reactee][react_str] += 1
                        except KeyError:
                            react_counts[reactor][reactee][react_str] = 1

                    else:
                        react_counts[reactor][reactee] += 1

                except KeyError:
                    # Reacter has left the group
                    # Could add logic for this but for now let's
                    # just raise because it shouldn't happen
                    raise

        except KeyError:
            # Message has no reactions
            pass

    return react_counts
