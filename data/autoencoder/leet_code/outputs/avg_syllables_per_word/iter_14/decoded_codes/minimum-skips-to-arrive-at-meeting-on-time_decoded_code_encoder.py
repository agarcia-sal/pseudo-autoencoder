import math
from typing import List

class Solution:
    def minSkips(self, dist: List[int], speed: int, hoursBefore: int) -> int:
        n = len(dist)
        INF = float('inf')
        dp = [[INF] * (n + 1) for _ in range(n)]

        total_dist = sum(dist)
        if total_dist / speed > hoursBefore:
            return -1

        dp[0][0] = dist[0]
        for j in range(1, n + 1):
            dp[0][j] = dist[0]  # dp[0][j] for j>0 are set, but realistically only dp[0][0] is needed, keeping as per pseudocode

        for i in range(1, n):
            for j in range(i + 1):
                if j <= i - 1:
                    # wait time rounding up to next integer hour (except for last segment) before adding dist[i]
                    prev = dp[i - 1][j]
                    if prev == INF:
                        continue
                    dp[i][j] = math.ceil(prev / speed) * speed + dist[i]
                if j > 0:
                    # skip waiting for this segment
                    dp[i][j] = min(dp[i][j], dp[i - 1][j - 1] + dist[i])

        for j in range(n + 1):
            if dp[n - 1][j] <= hoursBefore * speed:
                return j
        return -1