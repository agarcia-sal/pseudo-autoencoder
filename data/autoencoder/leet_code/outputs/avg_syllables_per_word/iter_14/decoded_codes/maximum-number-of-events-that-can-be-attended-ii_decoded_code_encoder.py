from bisect import bisect_left
from typing import List

class Solution:
    def maxValue(self, events: List[List[int]], k: int) -> int:
        # Sort events by their end day
        events.sort(key=lambda x: x[1])
        n = len(events)

        # Extract end times into a separate list for binary search
        ends = [event[1] for event in events]

        # Initialize dp with (n+1) rows and (k+1) columns filled with zeros
        dp = [[0] * (k + 1) for _ in range(n + 1)]

        for i in range(1, n + 1):
            start, end, value = events[i - 1]
            # Find the index j where events[j].end < start using bisect_left on ends, to find non-overlapping event
            j = bisect_left(ends, start)  # j is the first event ending >= start
            # We want events with end < start so bisect_left gives correct insertion point
            for l in range(1, k + 1):
                # Either skip current event or take it plus best up to j events with l-1 picks
                dp[i][l] = max(dp[i - 1][l], dp[j][l - 1] + value)

        return dp[n][k]