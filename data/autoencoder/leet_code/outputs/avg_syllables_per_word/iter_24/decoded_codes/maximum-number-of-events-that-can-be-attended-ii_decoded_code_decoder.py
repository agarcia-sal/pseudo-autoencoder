from bisect import bisect_left
from typing import List

class Solution:
    def maxValue(self, events: List[List[int]], k: int) -> int:
        events.sort(key=lambda e: e[1])
        n = len(events)
        ends = [e[1] for e in events]
        dp = [[0] * (k + 1) for _ in range(n + 1)]
        for i in range(1, n + 1):
            start, end, value = events[i - 1]
            j = bisect_left(ends, start)
            for l in range(1, k + 1):
                dp[i][l] = max(dp[i - 1][l], dp[j][l - 1] + value)
        return dp[n][k]