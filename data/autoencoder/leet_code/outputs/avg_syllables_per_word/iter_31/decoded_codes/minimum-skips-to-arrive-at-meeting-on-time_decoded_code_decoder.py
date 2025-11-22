from math import ceil
from typing import List

class Solution:
    def minSkips(self, dist: List[int], speed: int, hoursBefore: int) -> int:
        n = len(dist)
        INF = float('inf')

        # dp[i][j]: the minimal total distance traveled (including waiting) after i-th road,
        # with j skips used
        dp = [[INF] * (n + 1) for _ in range(n)]

        # Quick check: if minimal possible travel time (sum dist / speed) > hoursBefore, return -1
        total_dist = sum(dist)
        if total_dist > hoursBefore * speed:
            return -1

        # First road, no skip: no waiting needed
        dp[0][0] = dist[0]
        # First road, with skips > 0: same as no skip since skipping waiting is allowed
        for j in range(1, n + 1):
            dp[0][j] = dist[0]

        for i in range(1, n):
            for j in range(0, i + 1):
                # Not skipping waiting after previous road i-1 (except after last segment)
                val_without_skip = ceil(dp[i - 1][j] / speed) * speed + dist[i] if j <= i else INF
                dp[i][j] = min(dp[i][j], val_without_skip)

                # Skipping waiting after previous road i-1 (only if j > 0)
                if j > 0:
                    val_with_skip = dp[i - 1][j - 1] + dist[i]
                    dp[i][j] = min(dp[i][j], val_with_skip)

        # Find minimal skips j such that total time <= hoursBefore
        for j in range(n + 1):
            if dp[n - 1][j] <= hoursBefore * speed:
                return j

        return -1