from bisect import bisect_left
from typing import List

class Solution:
    def maxValue(self, events: List[List[int]], k: int) -> int:
        # Sort events by their end time (second element)
        events.sort(key=lambda x: x[1])
        n = len(events)

        # Prepare dp array: (n+1) x (k+1) initialized to 0
        dp = [[0] * (k + 1) for _ in range(n + 1)]

        # Extract end times to perform binary search on them
        ends = [event[1] for event in events]

        for i in range(1, n + 1):
            start, end, value = events[i - 1]
            # Find the last event index j where events[j].end < start
            # We use binary search to find insertion point of start in ends
            # bisect_left returns the position to insert start to keep ends sorted
            j = bisect_left(ends, start)  # events[j].end >= start, so j is the count of events ending before start

            for l in range(1, k + 1):
                dp[i][l] = max(dp[i - 1][l], dp[j][l - 1] + value)

        return dp[n][k]