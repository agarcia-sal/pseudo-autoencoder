from bisect import bisect_right
from typing import List

class Solution:
    def maxValue(self, events: List[List[int]], k: int) -> int:
        # Sort events by their end day
        events.sort(key=lambda x: x[1])
        n = len(events)
        dp = [[0] * (k + 1) for _ in range(n + 1)]

        # Extract end days to facilitate binary search
        end_days = [event[1] for event in events]

        for i in range(1, n + 1):
            start, end, value = events[i - 1]
            # Find position j where events[j-1].end < start
            j = bisect_right(end_days, start - 1)
            for l in range(1, k + 1):
                dp[i][l] = max(dp[i - 1][l], dp[j][l - 1] + value)

        return dp[n][k]