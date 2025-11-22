import math
from typing import List

class Solution:
    def minSkips(self, dist: List[int], speed: int, hoursBefore: int) -> int:
        n = len(dist)
        # dp[i][j]: minimum total distance sum achievable up to i-th segment with j skips
        # Initialize with infinity
        dp = [[math.inf] * (n + 1) for _ in range(n)]

        totalDist = sum(dist)
        # Quick check: if total time without any skips is more than allowed hours, no solution
        if totalDist / speed > hoursBefore:
            return -1

        # Base cases for the first segment
        dp[0][0] = dist[0]
        for j in range(1, n + 1):
            dp[0][j] = dist[0]

        for i in range(1, n):
            for j in range(0, i + 1):
                if j <= i - 1:
                    # No skip for i-th segment: round up time for (i-1)th segment with j skips,
                    # then add current segment distance
                    prev = dp[i - 1][j]
                    if prev == math.inf:
                        continue
                    # Compute arrival time after previous segments rounded up to next integer hour
                    prev_ceil = math.ceil(prev / speed) * speed
                    dp[i][j] = prev_ceil + dist[i]
                if j > 0:
                    # Skip the rounding after (i-1)th segment, add current segment distance
                    prev = dp[i - 1][j - 1]
                    if prev == math.inf:
                        continue
                    cand = prev + dist[i]
                    if cand < dp[i][j]:
                        dp[i][j] = cand

        for j in range(n + 1):
            if dp[n - 1][j] <= hoursBefore * speed:
                return j
        return -1