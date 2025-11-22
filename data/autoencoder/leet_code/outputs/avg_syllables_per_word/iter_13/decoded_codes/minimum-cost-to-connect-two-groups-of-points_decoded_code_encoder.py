from math import inf

class Solution:
    def connectTwoGroups(self, cost: list[list[int]]) -> int:
        size1 = len(cost)
        size2 = len(cost[0])
        max_mask = 1 << size2
        dp = [[inf] * max_mask for _ in range(size1 + 1)]
        dp[0][0] = 0

        for i in range(size1):
            for mask in range(max_mask):
                for j in range(size2):
                    combined_mask = mask | (1 << j)
                    dp[i + 1][combined_mask] = min(dp[i + 1][combined_mask], dp[i][mask] + cost[i][j])
                for j in range(size2):
                    if (mask & (1 << j)) != 0:
                        toggled_mask = mask ^ (1 << j)
                        dp[i + 1][mask] = min(dp[i + 1][mask], dp[i + 1][toggled_mask] + cost[i][j])

        return dp[size1][max_mask - 1]