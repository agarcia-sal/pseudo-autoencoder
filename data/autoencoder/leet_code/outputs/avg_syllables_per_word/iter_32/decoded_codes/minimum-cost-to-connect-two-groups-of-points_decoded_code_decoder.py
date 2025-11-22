from math import inf

class Solution:
    def connectTwoGroups(self, cost):
        size1 = len(cost)
        size2 = len(cost[0]) if cost else 0

        # dp[i][mask]: minimum cost to connect first i groups with mask representing connected points in second group
        dp = [[inf] * (1 << size2) for _ in range(size1 + 1)]
        dp[0][0] = 0

        for i in range(size1):
            for mask in range(1 << size2):
                cur_cost = dp[i][mask]
                if cur_cost == inf:
                    continue

                # Try connecting the i-th group to the j-th point in second group
                for j in range(size2):
                    index_mask_union = mask | (1 << j)
                    new_cost = cur_cost + cost[i][j]
                    if new_cost < dp[i + 1][index_mask_union]:
                        dp[i + 1][index_mask_union] = new_cost

                # Also consider the case where for already connected points in mask,
                # skip including current group's connection and only add cost for additional connections
                for j in range(size2):
                    bit = 1 << j
                    if mask & bit:
                        prev_mask = mask ^ bit
                        new_cost = dp[i + 1][prev_mask] + cost[i][j]
                        if new_cost < dp[i + 1][mask]:
                            dp[i + 1][mask] = new_cost

        return dp[size1][(1 << size2) - 1]