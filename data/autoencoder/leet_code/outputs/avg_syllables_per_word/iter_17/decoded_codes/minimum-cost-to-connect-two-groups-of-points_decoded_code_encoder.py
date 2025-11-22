from math import inf

class Solution:
    def connectTwoGroups(self, cost):
        size1 = len(cost)
        size2 = len(cost[0]) if cost else 0
        dp = self.initializeDPTable(size1, size2)
        dp[0][0] = 0

        for i in range(size1):
            for mask in range(1 << size2):
                current_dp = dp[i][mask]
                if current_dp == inf:
                    # Skip unreachable states
                    continue
                for j in range(size2):
                    new_mask = mask | (1 << j)
                    candidate_value = current_dp + cost[i][j]
                    if candidate_value < dp[i + 1][new_mask]:
                        dp[i + 1][new_mask] = candidate_value

                for j in range(size2):
                    if (mask & (1 << j)) > 0:
                        without_j_mask = mask ^ (1 << j)
                        candidate_value = dp[i + 1][without_j_mask] + cost[i][j]
                        if candidate_value < dp[i + 1][mask]:
                            dp[i + 1][mask] = candidate_value

        return dp[size1][(1 << size2) - 1]

    def initializeDPTable(self, size1, size2):
        length = 1 << size2
        return [[inf] * length for _ in range(size1 + 1)]

    def powerOfTwo(self, exponent):
        return 1 << exponent

    def infinity(self):
        return inf