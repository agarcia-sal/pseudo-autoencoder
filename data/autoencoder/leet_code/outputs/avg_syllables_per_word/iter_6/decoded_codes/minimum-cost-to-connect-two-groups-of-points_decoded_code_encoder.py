class Solution:
    def connectTwoGroups(self, cost):
        size1, size2 = len(cost), len(cost[0])
        INF = float('inf')
        dp = [[INF] * (1 << size2) for _ in range(size1 + 1)]
        dp[0][0] = 0

        for i in range(size1):
            for mask in range(1 << size2):
                cur = dp[i][mask]
                if cur == INF:
                    continue
                for j in range(size2):
                    next_mask = mask | (1 << j)
                    dp[i + 1][next_mask] = min(dp[i + 1][next_mask], cur + cost[i][j])
                for j in range(size2):
                    if mask & (1 << j):
                        alt_mask = mask ^ (1 << j)
                        dp[i + 1][mask] = min(dp[i + 1][mask], dp[i + 1][alt_mask] + cost[i][j])

        return dp[size1][(1 << size2) - 1]