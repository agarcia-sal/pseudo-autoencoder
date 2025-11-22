from math import inf

class Solution:
    def connectTwoGroups(self, cost: list[list[int]]) -> int:
        size1 = len(cost)
        size2 = len(cost[0])
        max_mask = 1 << size2
        dp = [[inf] * max_mask for _ in range(size1 + 1)]
        dp[0][0] = 0

        for i in range(size1):
            for mask in range(max_mask):
                current_dp_val = dp[i][mask]
                if current_dp_val == inf:
                    continue
                for j in range(size2):
                    current_mask = mask | (1 << j)
                    candidate_cost = current_dp_val + cost[i][j]
                    if candidate_cost < dp[i + 1][current_mask]:
                        dp[i + 1][current_mask] = candidate_cost

                for j in range(size2):
                    bit = 1 << j
                    if (mask & bit) != 0:
                        mask_without_j = mask ^ bit
                        candidate_cost = dp[i + 1][mask_without_j] + cost[i][j]
                        if candidate_cost < dp[i + 1][mask]:
                            dp[i + 1][mask] = candidate_cost

        return dp[size1][max_mask - 1]