from math import inf

class Solution:
    def connectTwoGroups(self, cost):
        size1 = len(cost)
        size2 = len(cost[0])
        max_mask = 1 << size2
        dp = [[inf] * max_mask for _ in range(size1 + 1)]
        dp[0][0] = 0

        for i in range(size1):
            for mask in range(max_mask):
                if dp[i][mask] == inf:
                    continue
                # Try connecting i-th element in group1 to j-th element in group2
                for j in range(size2):
                    new_mask = mask | (1 << j)
                    cur = dp[i][mask] + cost[i][j]
                    if cur < dp[i + 1][new_mask]:
                        dp[i + 1][new_mask] = cur
                # Try not connecting new element in group1 to any new group2 element,
                # but ensure mask covers group2 elements properly by merging previous states
                for j in range(size2):
                    if (mask & (1 << j)) != 0:
                        mask_without_j = mask ^ (1 << j)
                        cur = dp[i + 1][mask_without_j] + cost[i][j]
                        if cur < dp[i + 1][mask]:
                            dp[i + 1][mask] = cur

        return dp[size1][max_mask - 1]