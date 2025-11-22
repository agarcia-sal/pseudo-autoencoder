from math import inf
from typing import List

class Solution:
    def connectTwoGroups(self, cost: List[List[int]]) -> int:
        size1 = len(cost)
        size2 = len(cost[0]) if cost else 0

        dp = [[inf] * (1 << size2) for _ in range(size1 + 1)]
        dp[0][0] = 0

        for i in range(size1):
            for mask in range(1 << size2):
                if dp[i][mask] == inf:
                    continue
                # Try to connect cost group i with each element j in the second group,
                # adding j if it is not yet connected (mask updated)
                for j in range(size2):
                    masked_position = mask | (1 << j)
                    cost_val = cost[i][j]
                    if dp[i + 1][masked_position] > dp[i][mask] + cost_val:
                        dp[i + 1][masked_position] = dp[i][mask] + cost_val

                # Also try to connect cost group i members j that are already connected in mask,
                # possibly toggling them to minimize cost in next dp row.
                for j in range(size2):
                    if (mask & (1 << j)) != 0:
                        toggled_mask = mask ^ (1 << j)
                        cost_val = cost[i][j]
                        if dp[i + 1][mask] > dp[i + 1][toggled_mask] + cost_val:
                            dp[i + 1][mask] = dp[i + 1][toggled_mask] + cost_val

        return dp[size1][(1 << size2) - 1]