"""
Event Partitioner (by key)
Author: Yiru Fang
Description: Partition a stream of events by a given key function.
"""

from collections import defaultdict

def partition_events(events, key_fn):
    res =defaultdict(list)
    keys =[]
    for event in events:
        key = key_fn(event) 
        res[key].append(event)
    return res
    """
    Partition events into groups based on a key function.

    :param events: list of dict (or objects), each event has multiple attributes
    :param key_fn: function to extract the partition key from an event
    :return: dict {key: list of events}
    """
    # TODO: initialize a dictionary (defaultdict(list))
    # TODO: iterate over events, apply key_fn(event)
    # TODO: append event to the correct partition
    # TODO: return dictionary of partitions
    pass


# ===============================
# Example usage (after implementation)
# ===============================
if __name__ == "__main__":
    events = [
        {"device": "cam1", "val": 10},
        {"device": "cam2", "val": 20},
        {"device": "cam1", "val": 30},
    ]

    # Partition by device id
    result = partition_events(events, key_fn=lambda x: x["device"])
    print(result)
    # Expected:
    # {
    #   "cam1": [{"device":"cam1","val":10}, {"device":"cam1","val":30}],
    #   "cam2": [{"device":"cam2","val":20}]
    # }
