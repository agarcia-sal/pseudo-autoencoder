class Solution:
    def connectTwoGroups(self, cost: list[list[int]]) -> int:
        size1 = len(cost)
        size2 = len(cost[0]) if size1 > 0 else 0
        max_mask = 1 << size2
        dp = [[float('inf')] * max_mask for _ in range(size1 + 1)]
        dp[0][0] = 0

        for i in range(size1):
            for mask in range(max_mask):
                if dp[i][mask] == float('inf'):
                    continue
                # Connect node i in group1 to any node j in group2, updating new_mask
                for j in range(size2):
                    new_mask = mask | (1 << j)
                    dp[i + 1][new_mask] = min(dp[i + 1][new_mask], dp[i][mask] + cost[i][j])
                # Also consider toggling covered nodes in mask while connecting
                for j in range(size2):
                    if (mask & (1 << j)) != 0:
                        toggled_mask = mask ^ (1 << j)
                        dp[i + 1][mask] = min(dp[i + 1][mask], dp[i + 1][toggled_mask] + cost[i][j])

        return dp[size1][max_mask - 1]