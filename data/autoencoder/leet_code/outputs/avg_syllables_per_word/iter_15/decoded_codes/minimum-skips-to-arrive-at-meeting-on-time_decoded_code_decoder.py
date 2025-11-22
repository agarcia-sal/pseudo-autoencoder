import math
from typing import List

class Solution:
    def minSkips(self, dist: List[int], speed: int, hoursBefore: int) -> int:
        n = len(dist)

        def initialize_dp_matrix(rows: int, columns: int) -> List[List[float]]:
            # Create a 2D matrix filled with infinity
            return [[float('inf')] * columns for _ in range(rows)]

        dp = initialize_dp_matrix(n, n + 1)
        total_dist = sum(dist)

        # If minimum possible time (no waiting) exceeds hoursBefore return -1
        if total_dist / speed > hoursBefore:
            return -1

        # Base cases
        dp[0][0] = dist[0]
        for j in range(1, n + 1):
            dp[0][j] = dist[0]

        for i in range(1, n):
            for j in range(i + 1):
                if j <= i:
                    # without skip (round-up the time taken so far divided by speed and multiply by speed)
                    time_no_skip = math.ceil(dp[i - 1][j] / speed) * speed + dist[i]
                    dp[i][j] = time_no_skip
                if j > 0:
                    # with skip (no rounding up on previous)
                    time_skip = dp[i - 1][j - 1] + dist[i]
                    dp[i][j] = min(dp[i][j], time_skip)

        for j in range(n + 1):
            # If the time required with j skips is within the allowed time
            if dp[n - 1][j] <= hoursBefore * speed:
                return j

        return -1