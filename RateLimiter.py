"""
Rate Limiter Skeleton
Author: Yiru Fang
Description: Implement a sliding window rate limiter.
"""

import time
from collections import deque

class RateLimiter:
    def __init__(self, max_calls, window_sec):
        self.max_calls = max_calls
        self.rate =deque([])
        self.window_sec = window_sec
        """
        Initialize the rate limiter.
        :param max_calls: int, maximum allowed calls per window
        :param window_sec: int, size of the time window in seconds
        """
        # TODO: init variables
        pass

    def allow(self, timestamp=None):
        while self.rate and self.rate[0]<timestamp-self.window_sec:
            self.rate.popleft()
        if len(self.rate)== self.max_calls:
            return False
        else:
            self.rate.append(timestamp)
            return True
        
        """
        Check if the request at given timestamp is allowed.
        :param timestamp: float, seconds (if None, use current time)
        :return: bool, True if allowed, False otherwise
        """
        # TODO: implement sliding window logic
        pass


# ===============================
# Example usage (fill after implementation)
# ===============================
if __name__ == "__main__":
    rl = RateLimiter(max_calls=3, window_sec=5)
    print(rl.allow(1))   # Expected: True
    print(rl.allow(2))   # Expected: True
    print(rl.allow(3))   # Expected: True
    print(rl.allow(4))   # Expected: False
    print(rl.allow(7))   # Expected: True
