from bisect import bisect_left
from typing import List

class Solution:
    def maxValue(self, events: List[List[int]], k: int) -> int:
        # Sort events by end day (index 1)
        events.sort(key=lambda e: e[1])
        n = len(events)

        # Extract the end days for binary searching
        ends = [e[1] for e in events]

        # dp[i][l]: max value using first i events with up to l events chosen
        # Dimensions: (n+1) x (k+1), initialized to 0
        dp = [[0]*(k+1) for _ in range(n+1)]

        for i in range(1, n+1):
            start, end, value = events[i-1]
            # Find the leftmost index to insert start in ends to keep ends sorted
            # We search for start to find the last event that ends < start
            # bisect_left finds the first event ending >= start,
            # so events before that are non-conflicting, which is index j
            j = bisect_left(ends, start)

            for l in range(1, k+1):
                dp[i][l] = max(
                    dp[i-1][l],             # skip current event
                    dp[j][l-1] + value      # take current event after j-th event
                )
        return dp[n][k]