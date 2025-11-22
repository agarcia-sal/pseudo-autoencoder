class Solution:
    def connectTwoGroups(self, cost):
        size1, size2 = len(cost), len(cost[0])
        INF = float('inf')

        dp = [[INF] * (1 << size2) for _ in range(size1 + 1)]
        dp[0][0] = 0

        for i in range(size1):
            for mask in range(1 << size2):
                if dp[i][mask] == INF:
                    continue
                for j in range(size2):
                    new_mask = mask | (1 << j)
                    option_cost = dp[i][mask] + cost[i][j]
                    if option_cost < dp[i + 1][new_mask]:
                        dp[i + 1][new_mask] = option_cost
                for j in range(size2):
                    if (mask & (1 << j)) != 0:
                        alternative_cost = dp[i + 1][mask ^ (1 << j)] + cost[i][j]
                        if alternative_cost < dp[i + 1][mask]:
                            dp[i + 1][mask] = alternative_cost

        return dp[size1][(1 << size2) - 1]