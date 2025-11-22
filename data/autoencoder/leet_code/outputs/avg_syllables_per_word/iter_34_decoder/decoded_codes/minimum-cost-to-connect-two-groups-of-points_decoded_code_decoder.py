from math import inf

class Solution:
    def connectTwoGroups(self, cost):
        size1 = len(cost)
        size2 = len(cost[0])
        dp = [[inf] * (1 << size2) for _ in range(size1 + 1)]
        dp[0][0] = 0

        for i in range(size1):
            for mask in range(1 << size2):
                # Try connecting the i-th element in group1 to a new j-th element in group2
                for j in range(size2):
                    new_mask = mask | (1 << j)
                    dp[i + 1][new_mask] = min(dp[i + 1][new_mask], dp[i][mask] + cost[i][j])
                # Try not adding any new connection but possibly covering a previously connected j-th element
                for j in range(size2):
                    if mask & (1 << j):
                        new_mask = mask ^ (1 << j)
                        dp[i + 1][mask] = min(dp[i + 1][mask], dp[i + 1][new_mask] + cost[i][j])

        return dp[size1][(1 << size2) - 1]