"""
Problem 11: NBD (No Big Deal) Event Filter
Goal: Filter out low-importance events (e.g., repetitive pets) and keep actionable ones.
"""

from typing import Iterable, Any, Set, Dict, List

def filter_nbd(events: Iterable[Any], nbd_labels: Set[Any]) -> List[Any]:
    events = iter(events)
    res = []
    for event in events:
        if isinstance(event,str):
            if event not in nbd_labels:
                res.append(event)
        else:
            if event['type'] not in nbd_labels:
                res.append(event)
    return res

    """
    Remove events whose label/type is in nbd_labels.
    :param events: iterable of events; each event can be str or dict with a 'type' field
    :param nbd_labels: set of labels considered 'No Big Deal'
    :return: filtered list of events
    """
    # TODO: implement filtering logic
    # - If event is a dict, use event.get("type") to determine label
    # - If event is a str, use the str directly as label
    # - Return only non-NBD events
    raise NotImplementedError


# def dedup_within_window(events: Iterable[Dict], window_sec: float) -> List[Dict]:
#     """
#     Optional: remove near-duplicate events by (device_id, label) within window_sec.
#     :param events: list of dicts with fields: ts (float), device_id, type/label
#     :param window_sec: time window for deduplication
#     :return: deduplicated list
#     """
#     res = []
#     events = iter(events)
#     for event in events:
#         if events
#     # TODO: implement optional deduplication to reduce spam
#     raise NotImplementedError


if __name__ == "__main__":
    # TODO: add quick tests
    # Example:
    events = ["dog", "person", "car", "dog"]
    print(filter_nbd(events, {"dog"}))  # expected: ["person", "car"]
    pass