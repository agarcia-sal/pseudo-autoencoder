from math import inf

class Solution:
    def minDistance(self, houses, k):
        houses.sort()
        n = len(houses)

        def initialize_cost_matrix(size):
            return [[0] * size for _ in range(size)]

        cost = initialize_cost_matrix(n)

        # Precompute cost using prefix difference sums.
        for i in range(n - 1, -1, -1):
            for j in range(i + 1, n):
                cost[i][j] = cost[i + 1][j - 1] + houses[j] - houses[i]

        def initialize_dp_matrix(rows, cols):
            return [[inf] * cols for _ in range(rows)]

        dp = initialize_dp_matrix(n + 1, k + 1)
        dp[0][0] = 0

        for i in range(1, n + 1):
            for j in range(1, k + 1):
                for p in range(i):
                    current_value = dp[p][j - 1] + cost[p][i - 1]
                    if current_value < dp[i][j]:
                        dp[i][j] = current_value

        return dp[n][k]