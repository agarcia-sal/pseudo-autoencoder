from bisect import bisect_right
from typing import List

class Solution:
    def maxValue(self, events: List[List[int]], k: int) -> int:
        # Sort events by end day
        events.sort(key=lambda e: e[1])
        n = len(events)

        # Extract end days for binary search
        ends = [e[1] for e in events]

        # dp[i][l]: max value using first i events attending up to l events
        dp = [[0] * (k + 1) for _ in range(n + 1)]

        for i in range(1, n + 1):
            start, end, value = events[i - 1]
            # Find last event that ends before start day of current event
            j = bisect_right(ends, start - 1)
            for l in range(1, k + 1):
                dp[i][l] = max(dp[i - 1][l], dp[j][l - 1] + value)

        return dp[n][k]