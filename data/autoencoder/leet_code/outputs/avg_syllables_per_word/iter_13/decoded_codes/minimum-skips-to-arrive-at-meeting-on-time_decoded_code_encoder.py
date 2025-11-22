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

        # Initialize dp for the first segment with zero skips
        dp[0][0] = dist[0]

        # For zero skips and columns > 0, initial values set to dist[0]
        for j in range(1, n + 1):
            dp[0][j] = dist[0]

        for i in range(1, n):
            for j in range(i + 1):
                # Option when not skipping the current rest (j < i)
                if j < i:
                    # Ceiling of previous dp over speed times speed plus current segment distance
                    prev = dp[i-1][j]
                    dp[i][j] = math.ceil(prev / speed) * speed + dist[i]
                # Option when skipping current rest (j > 0)
                if j > 0:
                    dp[i][j] = min(dp[i][j], dp[i-1][j-1] + dist[i])

        for j in range(n + 1):
            if dp[n-1][j] <= hoursBefore * speed:
                return j

        return -1