import math
from typing import List

class Solution:
    def minSkips(self, dist: List[int], speed: int, hoursBefore: int) -> int:
        n = len(dist)
        dp = [[float('inf')] * (n + 1) for _ in range(n)]

        total_dist = sum(dist)
        if total_dist / speed > hoursBefore:
            return -1

        dp[0][0] = dist[0]
        for j in range(1, n):
            dp[0][j] = dist[0]

        for i in range(1, n):
            for j in range(i + 1):
                if j < i:
                    dp_value = dp[i-1][j]
                    divided_time = dp_value / speed
                    ceil_time = math.ceil(divided_time)
                    dp[i][j] = ceil_time * speed + dist[i]
                if j > 0:
                    skip_value = dp[i-1][j-1] + dist[i]
                    if skip_value < dp[i][j]:
                        dp[i][j] = skip_value

        for j in range(n + 1):
            if dp[n-1][j] <= hoursBefore * speed:
                return j

        return -1