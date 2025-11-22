from bisect import bisect_right
from typing import List

class Solution:
    def maxValue(self, events: List[List[int]], k: int) -> int:
        # Sort events by their end day
        events.sort(key=lambda x: x[1])
        n = len(events)

        # Extract end days for binary search
        end_days = [event[1] for event in events]

        # Initialize dp table with 0s; (n+1) x (k+1)
        dp = [[0] * (k + 1) for _ in range(n + 1)]

        for i in range(1, n + 1):
            start, end, value = events[i - 1]
            # Find the index j where events[j-1].end < start using bisect_right
            j = bisect_right(end_days, start - 1)

            for l in range(1, k + 1):
                # Either skip current event or take current event plus best from j events and l-1 picks
                dp[i][l] = max(dp[i - 1][l], dp[j][l - 1] + value)

        return dp[n][k]