from math import ceil
from typing import List

class Solution:
    def minSkips(self, dist: List[int], speed: int, hoursBefore: int) -> int:
        n = len(dist)
        INF = float('inf')
        # dp[i][j]: minimal total distance * speed (scaled) after i-th segment with j skips used
        # Using distance units before division by speed and ceiling adjustment for waiting at checkpoints
        dp = [[INF] * (n + 1) for _ in range(n)]
        total_dist = sum(dist)

        # If even without any wait, the total time exceeds hoursBefore, impossible
        if total_dist / speed > hoursBefore:
            return -1

        # Initialization: first segment with 0 skips — no waiting after first segment
        dp[0][0] = dist[0]
        for j in range(1, n):
            dp[0][j] = dist[0]

        for i in range(1, n):
            for j in range(i + 1):
                # If we don't skip the waiting after previous segment
                if j <= i - 1:
                    # Round up the time of previous to nearest integer hours, then add current segment distance
                    dp[i][j] = ceil(dp[i - 1][j] / speed) * speed + dist[i]
                # If we skip the waiting after previous segment (using one of the skips)
                if j > 0:
                    dp[i][j] = min(dp[i][j], dp[i - 1][j - 1] + dist[i])

        # Find minimal skips j where total time <= hoursBefore
        for j in range(n):
            if dp[n - 1][j] <= hoursBefore * speed:
                return j

        return -1