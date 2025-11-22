from math import inf

class Solution:
    def connectTwoGroups(self, cost: list[list[int]]) -> int:
        size1 = len(cost)
        size2 = len(cost[0])
        dp = [[inf] * (1 << size2) for _ in range(size1 + 1)]
        dp[0][0] = 0

        for i in range(size1):
            for mask in range(1 << size2):
                current = dp[i][mask]
                if current == inf:
                    continue
                # Connect group i to a new node in group 2
                for j in range(size2):
                    new_mask = mask | (1 << j)
                    dp[i + 1][new_mask] = min(dp[i + 1][new_mask], current + cost[i][j])
                # Optionally connect group i to an already connected node in group 2
                for j in range(size2):
                    bit = 1 << j
                    if mask & bit:
                        dp[i + 1][mask] = min(dp[i + 1][mask], dp[i + 1][mask ^ bit] + cost[i][j])

        return dp[size1][(1 << size2) - 1]