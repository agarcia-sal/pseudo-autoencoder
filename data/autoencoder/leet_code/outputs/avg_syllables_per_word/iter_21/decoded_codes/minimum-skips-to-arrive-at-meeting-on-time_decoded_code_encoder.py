import math

class Solution:
    def minSkips(self, dist, speed, hoursBefore):
        n = len(dist)
        # Initialize dp array with infinity
        dp = [[math.inf] * (n + 1) for _ in range(n)]
        total_dist = sum(dist)

        if total_dist / speed > hoursBefore:
            return -1

        # Base case: without any skips, cumulative distance after first segment
        dp[0][0] = dist[0]
        for j in range(1, n):
            dp[0][j] = dist[0]

        for i in range(1, n):
            for j in range(i + 1):
                if j < i:
                    # Without skip after i-th segment, wait until next integer hour
                    dp[i][j] = math.ceil(dp[i - 1][j] / speed) * speed + dist[i]
                if j > 0:
                    # Use a skip after i-th segment, no waiting needed
                    dp[i][j] = min(dp[i][j], dp[i - 1][j - 1] + dist[i])

        for j in range(n):
            if dp[n - 1][j] <= hoursBefore * speed:
                return j

        return -1