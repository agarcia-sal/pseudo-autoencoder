from typing import List

class Solution:
    def connectTwoGroups(self, cost: List[List[int]]) -> int:
        size1 = len(cost)
        size2 = len(cost[0]) if size1 > 0 else 0
        max_mask = 1 << size2
        INF = float('inf')

        dp = [[INF] * max_mask for _ in range(size1 + 1)]
        dp[0][0] = 0

        for i in range(size1):
            for mask in range(max_mask):
                current_cost = dp[i][mask]
                if current_cost == INF:
                    continue
                # Try to connect element i to each j, updating mask
                for j in range(size2):
                    position = mask | (1 << j)
                    new_cost = current_cost + cost[i][j]
                    if dp[i + 1][position] > new_cost:
                        dp[i + 1][position] = new_cost

                # Also try to skip connecting some elements that are already connected
                for j in range(size2):
                    if (mask & (1 << j)) != 0:
                        new_mask = mask ^ (1 << j)
                        possible_cost = dp[i + 1][new_mask] + cost[i][j]
                        if dp[i + 1][mask] > possible_cost:
                            dp[i + 1][mask] = possible_cost

        return dp[size1][max_mask - 1]