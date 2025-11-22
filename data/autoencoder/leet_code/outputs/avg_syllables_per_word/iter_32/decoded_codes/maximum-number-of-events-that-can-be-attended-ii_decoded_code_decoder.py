from bisect import bisect_left
from typing import List

class Solution:
    def maxValue(self, events: List[List[int]], k: int) -> int:
        # Sort events by their end day
        events.sort(key=lambda x: x[1])
        n = len(events)

        # Extract list of end days for binary searching
        end_days = [e[1] for e in events]

        # dp[i][l]: max value using first i events with up to l events chosen
        # Using (n+1) x (k+1) matrix filled with 0
        dp = [[0] * (k + 1) for _ in range(n + 1)]

        for i in range(1, n + 1):
            start, end, value = events[i - 1]
            # Find index j using binary search: largest j with end_days[j] < start
            # bisect_left(end_days, start) returns first index where end_days[idx] >= start
            j = bisect_left(end_days, start)

            for l in range(1, k + 1):
                dp[i][l] = max(dp[i - 1][l], dp[j][l - 1] + value)

        return dp[n][k]