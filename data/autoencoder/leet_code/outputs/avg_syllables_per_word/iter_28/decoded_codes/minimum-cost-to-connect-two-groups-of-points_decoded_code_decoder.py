from math import inf

class Solution:
    def connectTwoGroups(self, cost):
        size1 = len(cost)
        size2 = len(cost[0]) if size1 > 0 else 0
        dp = [[inf] * (1 << size2) for _ in range(size1 + 1)]
        dp[0][0] = 0

        for i in range(size1):
            for mask in range(1 << size2):
                current = dp[i][mask]
                if current == inf:
                    continue
                for j in range(size2):
                    new_mask = mask | (1 << j)
                    if dp[i + 1][new_mask] > current + cost[i][j]:
                        dp[i + 1][new_mask] = current + cost[i][j]
                for j in range(size2):
                    if (mask & (1 << j)) != 0:
                        alt_mask = mask ^ (1 << j)
                        if dp[i + 1][mask] > dp[i + 1][alt_mask] + cost[i][j]:
                            dp[i + 1][mask] = dp[i + 1][alt_mask] + cost[i][j]

        return dp[size1][(1 << size2) - 1]