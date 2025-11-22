class Solution:
    def connectTwoGroups(self, cost):
        size1 = len(cost)
        size2 = len(cost[0])

        dp = self.initializeDPTable(size1, size2)
        dp[0][0] = 0

        for i in range(size1):
            for mask in range(1 << size2):
                for j in range(size2):
                    combined_mask = mask | (1 << j)
                    candidate_cost = cost[i][j] + dp[i][mask]
                    current_cost = dp[i + 1][combined_mask]
                    if candidate_cost < current_cost:
                        dp[i + 1][combined_mask] = candidate_cost

                for j in range(size2):
                    if (mask & (1 << j)) != 0:
                        candidate_cost = dp[i + 1][mask ^ (1 << j)] + cost[i][j]
                        current_cost = dp[i + 1][mask]
                        if candidate_cost < current_cost:
                            dp[i + 1][mask] = candidate_cost

        full_mask = (1 << size2) - 1
        return dp[size1][full_mask]

    def initializeDPTable(self, size1, size2):
        return [[float('inf')] * (1 << size2) for _ in range(size1 + 1)]