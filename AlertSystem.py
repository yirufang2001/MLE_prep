"""
Problem 12: Alert System
Goal: Trigger an alert when 'anomaly' occurs >= threshold times consecutively.
"""

from typing import Iterable, Any

def detect_alerts(stream: Iterable[Any], anomaly_label: Any = "anomaly", threshold: int = 3) -> bool:
    stream = iter(stream)
    curr_c =0
    for event in stream:
        if event == anomaly_label:
            curr_c +=1
            if curr_c >=threshold:
                return True
        else:
            curr_c = 0
    return False



    """
    Return True if anomaly_label appears threshold times in a row.
    :param stream: iterable of labels or event dicts
    :param anomaly_label: the label that counts as anomaly
    :param threshold: consecutive count needed to trigger
    :return: bool
    """

    # TODO: implement consecutive counter
    # - If event is dict, read label from event.get("label") or event.get("type")
    raise NotImplementedError


def first_alert_index(stream: Iterable[Any], anomaly_label: Any = "anomaly", threshold: int = 3) -> int:
    stream = iter(stream)
    # curr_c =0
    curr_idx = 0
    for event in stream:
        if event == anomaly_label:
            return curr_idx
        curr_idx+=1
    return -1
    
    """
    Return index where the alert condition is first met; -1 if never.
    """
    # TODO: implement index tracking (0-based)
    raise NotImplementedError


if __name__ == "__main__":
    # TODO: add quick tests
    print(detect_alerts(["ok","anomaly","anomaly","anomaly"]))  # True
    pass