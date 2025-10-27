class Solution:
    def connectTwoGroups(self, cost):
        size1 = len(cost)
        size2 = len(cost[0]) if size1 > 0 else 0
        max_mask = 1 << size2

        # Initialize dp with infinity
        dp = [[float('inf')] * max_mask for _ in range(size1 + 1)]
        dp[0][0] = 0

        for i in range(size1):
            for mask in range(max_mask):
                current_cost = dp[i][mask]
                if current_cost == float('inf'):
                    continue  # Skip impossible states

                for j in range(size2):
                    new_mask = mask | (1 << j)
                    new_cost = current_cost + cost[i][j]
                    if dp[i + 1][new_mask] > new_cost:
                        dp[i + 1][new_mask] = new_cost

                # Try removing single connections from mask after processing current group member
                for j in range(size2):
                    if (mask & (1 << j)) != 0:
                        toggled_mask = mask ^ (1 << j)
                        new_cost = dp[i + 1][toggled_mask] + cost[i][j]
                        if dp[i + 1][mask] > new_cost:
                            dp[i + 1][mask] = new_cost

        return dp[size1][max_mask - 1]