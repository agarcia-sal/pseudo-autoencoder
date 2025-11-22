class Solution:
    def connectTwoGroups(self, cost):
        size1, size2 = len(cost), len(cost[0])
        max_mask = 1 << size2
        INF = float('inf')
        dp = [[INF] * max_mask for _ in range(size1 + 1)]
        dp[0][0] = 0

        for i in range(size1):
            for mask in range(max_mask):
                val = dp[i][mask]
                if val == INF:
                    continue
                for j in range(size2):
                    new_mask = mask | (1 << j)
                    dp[i + 1][new_mask] = min(dp[i + 1][new_mask], val + cost[i][j])
                cur = dp[i + 1][mask]
                for j in range(size2):
                    if mask & (1 << j):
                        dp[i + 1][mask] = min(dp[i + 1][mask], cur ^ (1 << j) + cost[i][j])

        return dp[size1][max_mask - 1]