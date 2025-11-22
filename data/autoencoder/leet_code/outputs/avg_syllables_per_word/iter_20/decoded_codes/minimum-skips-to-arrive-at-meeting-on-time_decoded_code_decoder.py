import math
from typing import List

class Solution:
    def minSkips(self, dist: List[int], speed: int, hoursBefore: int) -> int:
        n = len(dist)
        INF = float('inf')
        dp = [[INF] * (n + 1) for _ in range(n)]

        total_dist = sum(dist)
        if total_dist > hoursBefore * speed:
            return -1

        dp[0][0] = dist[0]
        for j in range(1, n):
            dp[0][j] = dist[0]

        for i in range(1, n):
            for j in range(i + 1):
                if j < i:
                    # Wait for next integer hour for previous segment (skip next here)
                    prev = dp[i - 1][j]
                    dp[i][j] = (math.ceil(prev / speed) * speed) + dist[i]
                if j > 0:
                    # Skip waiting for this segment
                    dp[i][j] = min(dp[i][j], dp[i - 1][j - 1] + dist[i])

        for j in range(n):
            if dp[n - 1][j] <= hoursBefore * speed:
                return j
        return -1