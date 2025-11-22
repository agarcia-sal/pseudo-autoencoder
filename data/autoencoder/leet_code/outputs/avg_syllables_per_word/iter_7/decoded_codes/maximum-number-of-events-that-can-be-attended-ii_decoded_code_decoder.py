from typing import List, Tuple
import bisect

class Solution:
    def maxValue(self, events: List[Tuple[int, int, int]], k: int) -> int:
        events.sort(key=lambda x: x[1])  # sort by end day
        n = len(events)
        dp = [[0] * (k + 1) for _ in range(n + 1)]

        ends = [e[1] for e in events]
        for i in range(1, n + 1):
            start, end, value = events[i - 1]
            j = bisect.bisect_left(ends, start) - 1
            for l in range(1, k + 1):
                dp[i][l] = max(dp[i - 1][l], dp[j + 1][l - 1] + value if j >= 0 else value)

        return dp[n][k]