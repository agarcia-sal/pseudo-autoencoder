import math
from typing import List

class Solution:
    def minSkips(self, dist: List[int], speed: int, hoursBefore: int) -> int:
        n = len(dist)
        INF = float('inf')
        dp = [[INF] * (n + 1) for _ in range(n)]

        total_dist = sum(dist)
        if total_dist > speed * hoursBefore:
            return -1

        dp[0][0] = dist[0]
        for j in range(1, n):
            dp[j][0] = dist[0]

        for i in range(1, n):
            for j in range(i + 1):
                if j < i:
                    prev = dp[i - 1][j]
                    # ceil division adjusted to next multiple of speed
                    dp[i][j] = math.ceil(prev / speed) * speed + dist[i]
                if j > 0:
                    dp[i][j] = min(dp[i][j], dp[i - 1][j - 1] + dist[i])

        for j in range(n):
            if dp[n - 1][j] <= speed * hoursBefore:
                return j

        return -1