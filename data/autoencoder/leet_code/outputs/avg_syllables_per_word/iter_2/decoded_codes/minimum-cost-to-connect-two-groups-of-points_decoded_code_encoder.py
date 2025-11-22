class Solution:
    def connectTwoGroups(self, cost):
        size1 = len(cost)
        size2 = len(cost[0])

        dp = [[float('inf')] * (1 << size2) for _ in range(size1 + 1)]
        dp[0][0] = 0

        for i in range(size1):
            for mask in range(1 << size2):
                # Connect group1[i] to new group2 points
                for j in range(size2):
                    new_mask = mask | (1 << j)
                    dp[i + 1][new_mask] = min(dp[i + 1][new_mask], dp[i][mask] + cost[i][j])

                # Optimize connections by removing already covered points in current mask
                for j in range(size2):
                    if mask & (1 << j):
                        dp[i + 1][mask] = min(dp[i + 1][mask], dp[i + 1][mask ^ (1 << j)] + cost[i][j])

        return dp[size1][(1 << size2) - 1]