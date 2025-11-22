from typing import List

class Solution:
    def connectTwoGroups(self, cost: List[List[int]]) -> int:
        size1 = len(cost)
        size2 = len(cost[0]) if cost else 0
        full_mask = (1 << size2) - 1
        INF = float('inf')

        # dp[i][mask] = minimum cost to connect first i groups from group1
        # and mask represents the subset of group2 already connected
        dp = [[INF] * (1 << size2) for _ in range(size1 + 1)]
        dp[0][0] = 0

        for i in range(size1):
            for mask in range(1 << size2):
                if dp[i][mask] == INF:
                    continue

                for j in range(size2):
                    combined_mask = mask | (1 << j)
                    new_cost = dp[i][mask] + cost[i][j]
                    if dp[i + 1][combined_mask] > new_cost:
                        dp[i + 1][combined_mask] = new_cost

                # Consider toggling already connected j-th point in group2 for improvements
                for j in range(size2):
                    if (mask & (1 << j)) != 0:
                        toggled_mask = mask ^ (1 << j)
                        new_cost = dp[i + 1][toggled_mask] + cost[i][j]
                        if dp[i + 1][mask] > new_cost:
                            dp[i + 1][mask] = new_cost

        return dp[size1][full_mask]