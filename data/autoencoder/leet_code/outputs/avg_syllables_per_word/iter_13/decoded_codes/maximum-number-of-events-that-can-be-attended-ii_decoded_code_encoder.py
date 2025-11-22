from bisect import bisect_left
from typing import List

class Solution:
    def maxValue(self, events: List[List[int]], k: int) -> int:
        # Sort events by their end day (events[i][1])
        events.sort(key=lambda x: x[1])
        n = len(events)

        # Extract the end days for binary search
        ends = [event[1] for event in events]

        # dp[i][l]: max value attainable using first i events with at most l events
        dp = [[0] * (k + 1) for _ in range(n + 1)]

        for i in range(1, n + 1):
            start, end, value = events[i - 1]
            # Find the index j where events[j].end < start using bisect_left on ends
            j = bisect_left(ends, start, 0, i - 1)
            for l in range(1, k + 1):
                dp[i][l] = max(dp[i - 1][l], dp[j][l - 1] + value)

        return dp[n][k]