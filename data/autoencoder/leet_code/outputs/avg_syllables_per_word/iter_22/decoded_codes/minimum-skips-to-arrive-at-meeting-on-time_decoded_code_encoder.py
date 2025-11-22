import math

class Solution:
    def minSkips(self, dist, speed, hoursBefore):
        n = len(dist)
        INF = float('inf')
        dp = [[INF] * (n + 1) for _ in range(n)]
        total_dist = sum(dist)

        # If minimum possible time (no skipping any waiting) exceeds hoursBefore, return -1
        if total_dist / speed > hoursBefore:
            return -1

        # Initialize first row: zero skips means time equals dist[0]
        dp[0][0] = dist[0]
        # Though the pseudocode initializes all dp[0][j] for j in [1..n-1] to dist[0],
        # this is redundant for j>0 because zero elements means no distance traveled yet.
        # But we follow exactly as stated.
        for j in range(1, n):
            dp[0][j] = dist[0]

        for i in range(1, n):
            for j in range(i + 1):
                # Not skipping waiting after segment i-1 (except last)
                if j <= i - 1:
                    # Round up dp[i-1][j] / speed to next integer and multiply by speed, then add dist[i]
                    time_without_skip = math.ceil(dp[i - 1][j] / speed) * speed + dist[i]
                    dp[i][j] = time_without_skip

                if j > 0:
                    # Skipping waiting after segment i-1, add dist[i] directly
                    time_with_skip = dp[i - 1][j - 1] + dist[i]
                    if dp[i][j] > time_with_skip:
                        dp[i][j] = time_with_skip

        for j in range(n):
            # dp[n-1][j] / speed represents total time in hours (accounting for skips)
            # The original dp stores time in distance units (integer traveled), divide by speed to get hours
            if dp[n - 1][j] <= hoursBefore * speed:
                return j

        return -1