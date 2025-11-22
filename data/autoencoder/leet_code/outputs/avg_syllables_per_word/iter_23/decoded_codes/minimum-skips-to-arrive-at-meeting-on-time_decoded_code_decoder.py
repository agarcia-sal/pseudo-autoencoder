import math
from typing import List

class Solution:
    def minSkips(self, dist: List[int], speed: int, hoursBefore: int) -> int:
        n = len(dist)
        INF = float('inf')
        # dp[i][j]: minimum time in distance units to reach segment i using j skips
        dp = [[INF] * (n + 1) for _ in range(n)]
        total_dist = sum(dist)

        # If even total_dist/speed > hoursBefore, impossible no matter what
        if total_dist > hoursBefore * speed:
            return -1

        # Base case:
        dp[0][0] = dist[0]
        for j in range(1, n + 1):
            dp[0][j] = dist[0]

        for i in range(1, n):
            for j in range(0, i + 1):
                # Option 1: no skip at i segment, must wait for ceiling
                if j <= i - 1:
                    # ceil of dp[i-1][j]/speed * speed + dist[i]
                    time_no_skip = math.ceil(dp[i - 1][j] / speed) * speed + dist[i]
                    dp[i][j] = min(dp[i][j], time_no_skip)
                # Option 2: skip waiting at this segment, if skips available
                if j > 0:
                    time_skip = dp[i - 1][j - 1] + dist[i]
                    if time_skip < dp[i][j]:
                        dp[i][j] = time_skip

        for j in range(n + 1):
            if dp[n - 1][j] <= hoursBefore * speed:
                return j

        return -1