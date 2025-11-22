from bisect import bisect_left
from typing import List

class Solution:
    def maxValue(self, events: List[List[int]], k: int) -> int:
        # Sort events by end day ascending
        events.sort(key=lambda e: e[1])
        n = len(events)

        # Extract end times separately for binary search
        ends = [e[1] for e in events]

        # dp[i][l]: max value by considering first i events with at most l events chosen
        # Using (n+1) x (k+1) dp table filled with 0
        dp = [[0] * (k + 1) for _ in range(n + 1)]

        for i in range(1, n + 1):
            start, end, value = events[i - 1]
            # Find leftmost position j in events where events[j].end >= start
            # events are sorted by end day, so using binary search
            j = bisect_left(ends, start)
            for l in range(1, k + 1):
                # Two options: skip current event or take current event + dp of j events with l-1 selected
                dp[i][l] = max(dp[i - 1][l], dp[j][l - 1] + value)

        return dp[n][k]