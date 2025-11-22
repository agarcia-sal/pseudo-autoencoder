from bisect import bisect_right
from typing import List

class Solution:
    def maxValue(self, events: List[List[int]], k: int) -> int:
        events.sort(key=lambda x: x[1])  # sort by end day
        n = len(events)

        # Extract end days for binary search
        end_days = [e[1] for e in events]

        # dp[i][l]: max value picking up to l events among first i events
        dp = [[0] * (k + 1) for _ in range(n + 1)]

        for i in range(1, n + 1):
            start, end, value = events[i - 1]
            # Find the rightmost event that ends before start
            # bisect_right returns insertion position, so subtract 1 to get index
            j = bisect_right(end_days, start - 1)

            for l in range(1, k + 1):
                # Either skip current event or take it plus dp from j events with l-1 events selected
                dp[i][l] = max(dp[i - 1][l], dp[j][l - 1] + value)

        return dp[n][k]