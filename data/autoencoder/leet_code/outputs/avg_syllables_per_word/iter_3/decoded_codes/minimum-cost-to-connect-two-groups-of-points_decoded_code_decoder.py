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
                base = dp[i][mask]
                for j in range(size2):
                    new_mask = mask | (1 << j)
                    dp[i + 1][new_mask] = min(dp[i + 1][new_mask], base + cost[i][j])
                for j in range(size2):
                    bit = 1 << j
                    if mask & bit:
                        dp[i + 1][mask] = min(dp[i + 1][mask], dp[i + 1][mask ^ bit] + cost[i][j])

        return dp[size1][(1 << size2) - 1]