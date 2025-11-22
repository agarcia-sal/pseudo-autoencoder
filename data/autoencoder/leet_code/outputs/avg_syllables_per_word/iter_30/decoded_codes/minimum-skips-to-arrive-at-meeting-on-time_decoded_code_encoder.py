import math

class Solution:
    def minSkips(self, dist, speed, hoursBefore):
        n = len(dist)
        INF = float('inf')
        dp = [[INF] * (n + 1) for _ in range(n)]
        total_dist = sum(dist)

        if total_dist / speed > hoursBefore:
            return -1

        dp[0][0] = dist[0]
        for j in range(1, n + 1):
            dp[0][j] = dist[0]

        for i in range(1, n):
            for j in range(0, i + 1):
                if j < i:
                    prev = dp[i - 1][j]
                    # Time before adding current dist, rounded up to next integer
                    # then multiplied back by speed to get equivalent distance including waiting
                    dp[i][j] = math.ceil(prev / speed) * speed + dist[i]

                if j > 0:
                    no_wait = dp[i - 1][j - 1] + dist[i]
                    if no_wait < dp[i][j]:
                        dp[i][j] = no_wait

        for j in range(n + 1):
            if dp[n - 1][j] <= hoursBefore * speed:
                return j

        return -1