from bisect import bisect_left
from typing import List, Tuple

class Solution:
    def maxValue(self, events: List[Tuple[int, int, int]], k: int) -> int:
        # Sort events by their end time
        events.sort(key=lambda x: x[1])
        n = len(events)

        # Precompute list of event end times for binary search
        ends = [e[1] for e in events]

        # dp[i][l]: max value using first i events with at most l events chosen
        # dp has (n+1) rows and (k+1) columns, initialized to 0
        dp = [[0] * (k + 1) for _ in range(n + 1)]

        for i in range(1, n + 1):
            start, end, value = events[i - 1]
            # Find the position j where events[j].end >= start using binary search
            # We want the leftmost j where events[j].end >= start
            # Since events are sorted by end, we can use bisect_left on ends array
            j = bisect_left(ends, start)

            for l in range(1, k + 1):
                # Two choices:
                # 1. Not selecting the i-th event: dp[i-1][l]
                # 2. Selecting the i-th event: dp[j][l-1] + value
                dp[i][l] = max(dp[i-1][l], dp[j][l-1] + value)

        return dp[n][k]