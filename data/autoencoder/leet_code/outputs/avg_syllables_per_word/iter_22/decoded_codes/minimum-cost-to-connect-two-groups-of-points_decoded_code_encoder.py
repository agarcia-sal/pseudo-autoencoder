from math import inf

class Solution:
    def connectTwoGroups(self, cost):
        size1 = len(cost)
        size2 = len(cost[0])
        max_mask = 1 << size2

        # dp[i][mask]: minimum cost to connect first i groups and covering set 'mask' of second groups
        dp = [[inf] * max_mask for _ in range(size1 + 1)]
        dp[0][0] = 0

        for i in range(size1):
            for mask in range(max_mask):
                # Connect point i in the first group to some points in the second group (adding j)
                for j in range(size2):
                    current_mask = mask | (1 << j)
                    dp[i + 1][current_mask] = min(dp[i + 1][current_mask], dp[i][mask] + cost[i][j])

                # Try to reduce redundancy by possibly removing connections if mask has that j set
                for j in range(size2):
                    if (mask & (1 << j)) > 0:
                        new_mask = mask ^ (1 << j)
                        dp[i + 1][mask] = min(dp[i + 1][mask], dp[i + 1][new_mask] + cost[i][j])

        return dp[size1][max_mask - 1]