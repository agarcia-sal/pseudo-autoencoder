import math
from typing import List

class Solution:
    def minSkips(self, dist: List[int], speed: int, hoursBefore: int) -> int:
        n = len(dist)
        INF = float('inf')
        # dp[i][j]: minimum total time * speed to reach the end of i-th road with j skips
        dp = [[INF] * (n + 1) for _ in range(n)]

        total_dist = sum(dist)
        # If minimal possible time exceeds hoursBefore, no solution
        if total_dist > speed * hoursBefore:
            return -1

        # Initialize first segment: no rounding yet considered
        dp[0][0] = dist[0]
        for j in range(1, n + 1):
            dp[0][j] = dist[0]

        for i in range(1, n):
            for j in range(i + 1):
                if j <= i - 1:
                    # No skip at this segment: round up previous time to next full hour, then add current segment distance
                    prev = dp[i - 1][j]
                    dp[i][j] = math.ceil(prev / speed) * speed + dist[i] if prev != INF else INF
                if j > 0:
                    # Skip the waiting after previous segment (use skip), add current segment distance directly
                    prev_skip = dp[i - 1][j - 1]
                    if prev_skip != INF:
                        dp[i][j] = min(dp[i][j], prev_skip + dist[i])

        # Find minimal skips j for which total time/speed <= hoursBefore
        for j in range(n + 1):
            if dp[n - 1][j] <= hoursBefore * speed:
                return j

        return -1