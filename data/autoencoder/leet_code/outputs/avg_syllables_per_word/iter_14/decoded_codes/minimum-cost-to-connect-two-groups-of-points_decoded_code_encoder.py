from math import inf

class Solution:
    def connectTwoGroups(self, cost):
        size1 = len(cost)
        size2 = len(cost[0])

        dp = self.initialize_dp_table(size1, size2)
        dp[0][0] = 0

        for i in range(size1):
            for mask in range(1 << size2):
                cur_cost = dp[i][mask]
                if cur_cost == inf:
                    continue
                for j in range(size2):
                    new_mask = mask | (1 << j)
                    potential_cost = cost[i][j] + cur_cost
                    if dp[i + 1][new_mask] > potential_cost:
                        dp[i + 1][new_mask] = potential_cost
                for j in range(size2):
                    bit = 1 << j
                    if (mask & bit) != 0:
                        alternate_mask = mask ^ bit
                        potential_cost = dp[i + 1][alternate_mask] + cost[i][j]
                        if dp[i + 1][mask] > potential_cost:
                            dp[i + 1][mask] = potential_cost

        all_connected_mask = (1 << size2) - 1
        return dp[size1][all_connected_mask]

    def initialize_dp_table(self, size1, size2):
        return [[inf] * (1 << size2) for _ in range(size1 + 1)]