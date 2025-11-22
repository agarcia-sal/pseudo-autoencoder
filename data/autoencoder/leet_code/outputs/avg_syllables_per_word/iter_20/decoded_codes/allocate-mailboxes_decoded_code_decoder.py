from math import inf

class Solution:
    def minDistance(self, houses, k):
        houses.sort()
        n = len(houses)

        cost = [[0] * n for _ in range(n)]
        # Precompute cost for placing one mailbox for houses[i..j]
        # The cost is sum of distances to the median house's position
        for i in range(n - 1, -1, -1):
            for j in range(i + 1, n):
                cost[i][j] = cost[i + 1][j - 1] + houses[j] - houses[i]

        dp = [[inf] * (k + 1) for _ in range(n + 1)]
        dp[0][0] = 0

        for i in range(1, n + 1):
            for j in range(1, k + 1):
                for p in range(i):
                    curr = dp[p][j - 1] + cost[p][i - 1] if p <= i - 1 else inf
                    if curr < dp[i][j]:
                        dp[i][j] = curr

        return dp[n][k]