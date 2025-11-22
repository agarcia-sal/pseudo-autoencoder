class Solution:
    def connectTwoGroups(self, cost):
        size_one = len(cost)
        size_two = len(cost[0])

        MAX_MASK = 1 << size_two
        dp = [[float('inf')] * MAX_MASK for _ in range(size_one + 1)]
        dp[0][0] = 0

        for i in range(size_one):
            for mask in range(MAX_MASK):
                if dp[i][mask] == float('inf'):
                    continue
                for j in range(size_two):
                    new_mask = mask | (1 << j)
                    # Connect group i to element j in group two
                    dp[i + 1][new_mask] = min(dp[i + 1][new_mask], dp[i][mask] + cost[i][j])
                # Try to skip connecting new element in group two if already connected
                for j in range(size_two):
                    if (mask & (1 << j)) != 0:
                        dp[i + 1][mask] = min(dp[i + 1][mask], dp[i + 1][mask ^ (1 << j)] + cost[i][j])

        return dp[size_one][MAX_MASK - 1]