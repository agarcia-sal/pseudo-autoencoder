from bisect import bisect_left
from typing import List

class Solution:
    def maxValue(self, events: List[List[int]], k: int) -> int:
        # Sort events by their end time
        events.sort(key=lambda e: e[1])
        n = len(events)
        # dp[i][l] = max value using first i events with at most l events chosen
        dp = [[0] * (k + 1) for _ in range(n + 1)]

        # Extract end times for binary search
        ends = [e[1] for e in events]

        for i in range(1, n + 1):
            start, end, value = events[i - 1]
            # Find rightmost event that ends before start using binary search
            j = bisect_left(ends, start)
            for l in range(1, k + 1):
                # Check if not taking current event yields better or equal value
                if dp[i - 1][l] >= dp[j][l - 1] + value:
                    dp[i][l] = dp[i - 1][l]
                else:
                    dp[i][l] = dp[j][l - 1] + value

        return dp[n][k]