from math import inf

class Solution:
    def connectTwoGroups(self, cost):
        size1 = len(cost)
        size2 = len(cost[0])
        dp = [[inf] * (1 << size2) for _ in range(size1 + 1)]
        dp[0][0] = 0

        for i in range(size1):
            for mask in range(1 << size2):
                if dp[i][mask] == inf:
                    continue
                for j in range(size2):
                    new_mask = mask | (1 << j)
                    val = dp[i][mask] + cost[i][j]
                    if val < dp[i+1][new_mask]:
                        dp[i+1][new_mask] = val
                for j in range(size2):
                    if (mask & (1 << j)) != 0:
                        new_mask = mask ^ (1 << j)
                        val = dp[i+1][new_mask] + cost[i][j]
                        if val < dp[i+1][mask]:
                            dp[i+1][mask] = val

        return dp[size1][(1 << size2) - 1]