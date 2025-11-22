from math import inf

class Solution:
    def connectTwoGroups(self, cost):
        size1 = len(cost)
        size2 = len(cost[0])

        dp = self.initialize_dp_table(size1, size2)
        dp[0][0] = 0

        for i in range(size1):
            for mask in range(1 << size2):
                for j in range(size2):
                    new_mask = mask | (1 << j)
                    dp[i + 1][new_mask] = min(dp[i + 1][new_mask], dp[i][mask] + cost[i][j])

                for j in range(size2):
                    if (mask & (1 << j)) != 0:
                        dp[i + 1][mask] = min(dp[i + 1][mask], dp[i + 1][mask ^ (1 << j)] + cost[i][j])

        return dp[size1][(1 << size2) - 1]

    def initialize_dp_table(self, size1, size2):
        dp = []
        length = 1 << size2
        for _ in range(size1 + 1):
            dp.append([inf] * length)
        return dp