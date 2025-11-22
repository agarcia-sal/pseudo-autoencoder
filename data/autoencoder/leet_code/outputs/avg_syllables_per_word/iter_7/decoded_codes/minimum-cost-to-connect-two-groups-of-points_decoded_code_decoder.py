from typing import List

class Solution:
    def connectTwoGroups(self, cost: List[List[int]]) -> int:
        size1 = len(cost)
        size2 = len(cost[0])
        max_mask = 1 << size2
        INF = float('inf')
        dp = [[INF] * max_mask for _ in range(size1 + 1)]
        dp[0][0] = 0

        for i in range(size1):
            for mask in range(max_mask):
                if dp[i][mask] == INF:
                    continue
                for j in range(size2):
                    new_mask = mask | (1 << j)
                    dp[i + 1][new_mask] = min(dp[i + 1][new_mask], dp[i][mask] + cost[i][j])
                for j in range(size2):
                    if mask & (1 << j):
                        prev_mask = mask ^ (1 << j)
                        dp[i + 1][mask] = min(dp[i + 1][mask], dp[i + 1][prev_mask] + cost[i][j])

        return dp[size1][max_mask - 1]