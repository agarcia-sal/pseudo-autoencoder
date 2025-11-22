import math
from typing import List

class Solution:
    def minSkips(self, dist: List[int], speed: int, hoursBefore: int) -> int:
        n = len(dist)
        INF = float('inf')
        # dp[i][j] represents the minimum total distance traveled up to segment i with j skips
        dp = [[INF] * (n + 1) for _ in range(n)]

        total_dist = sum(dist)
        # If even without any waiting, total travel time exceeds hoursBefore, return -1
        if total_dist / speed > hoursBefore:
            return -1

        dp[0][0] = dist[0]
        for j in range(1, n):
            dp[0][j] = dist[0]

        for i in range(1, n):
            for j in range(i + 1):
                if j < i:
                    # No skip at segment i-1, round up previous distance/speed
                    prev = dp[i - 1][j]
                    if prev == INF:
                        continue
                    rounded = (math.ceil(prev / speed) * speed)
                    dp[i][j] = min(dp[i][j], rounded + dist[i])
                if j > 0:
                    # Skip waiting at segment i-1
                    prev_skip = dp[i - 1][j - 1]
                    if prev_skip == INF:
                        continue
                    dp[i][j] = min(dp[i][j], prev_skip + dist[i])

        for j in range(n + 1):
            if dp[n - 1][j] <= hoursBefore * speed:
                return j

        return -1