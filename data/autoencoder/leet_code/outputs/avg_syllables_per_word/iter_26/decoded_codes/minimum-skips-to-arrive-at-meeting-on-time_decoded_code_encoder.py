from math import ceil
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
            dp[0][j] = dist[0]

        for i in range(1, n):
            for j in range(i + 1):
                if j < i:
                    # Wait until you hit next integer hour before starting next segment,
                    # hence rounding up the previous time by speed before adding new dist.
                    dp[i][j] = ceil(dp[i - 1][j] / speed) * speed + dist[i]
                if j > 0:
                    # Use skip, so no waiting, just add dist
                    dp[i][j] = min(dp[i][j], dp[i - 1][j - 1] + dist[i])

        for j in range(n + 1):
            # Check if total time is less than or equal to allowed time scaled by speed
            if dp[n - 1][j] <= hoursBefore * speed:
                return j

        return -1