import math
from typing import List

class Solution:
    def minSkips(self, dist: List[int], speed: int, hoursBefore: int) -> int:
        n = len(dist)
        INF = float('inf')
        dp = [[INF] * (n + 1) for _ in range(n)]
        total_dist = sum(dist)

        # If even without stops we can't arrive in time
        if total_dist > speed * hoursBefore:
            return -1

        # Initialize dp for the first segment
        for j in range(n):
            dp[0][j] = dist[0]

        for i in range(1, n):
            for j in range(i + 1):
                if j < i:
                    # No skip on this segment: round up the previous cumulative time
                    dp[i][j] = math.ceil(dp[i - 1][j] / speed) * speed + dist[i]
                if j > 0:
                    # Skip on this segment: accumulate time without rounding previous arrival time
                    dp[i][j] = min(dp[i][j], dp[i - 1][j - 1] + dist[i])

        for j in range(n):
            if dp[n - 1][j] <= speed * hoursBefore:
                return j

        return -1