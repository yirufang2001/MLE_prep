"""
Problem 13: Priority-based Queue
Goal: Push items with priority; pop highest-priority first (max-heap behavior).
"""

from typing import Any, Optional, Tuple
import heapq

class PriorityQueue:
    def __init__(self):
        self.pq=[]
        """
        Initialize internal structure (e.g., heap).
        """
        # TODO: init heap (list), maybe a counter for FIFO within same priority
        # raise NotImplementedError

    def push(self, item: Any, priority: int) -> None:
        heapq.heappush(self.pq,(-priority,item))
        """
        Insert an item with priority (higher means more urgent).
        :param item: payload
        :param priority: integer priority; larger = higher priority
        """
        # TODO: heappush using negative priority or custom tuple
        # raise NotImplementedError

    def pop(self) -> Optional[Any]:
        if not self.pq:
            return 
        _,item = heapq.heappop(self.pq)
        return item
        """
        Pop the item with highest priority; return None if empty.
        """
        # TODO: heappop and return item
        raise NotImplementedError

    def peek(self) -> Optional[Tuple[int, Any]]:
        if not self.pq:
            return 
        _,item = self.pq[0]
        return item
        """
        Peek at current highest priority item without removal.
        :return: (priority, item) or None
        """
        # TODO: read top element without popping
        raise NotImplementedError

    def __len__(self) -> int:
        return len(self.pq)
        # TODO: return size
        raise NotImplementedError


if __name__ == "__main__":
    # TODO: add quick tests
    pq = PriorityQueue()
    pq.push("normal", 1)
    pq.push("urgent", 10)
    print(pq.pop() == "urgent")
    # pass