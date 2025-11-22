from math import inf

class Solution:
    def connectTwoGroups(self, cost):
        size1 = len(cost)
        size2 = len(cost[0]) if cost else 0

        # dp[i][mask]: minimal cost after connecting first i groups from group1,
        # with connected nodes from group2 represented by bitmask `mask`
        dp = [[inf] * (1 << size2) for _ in range(size1 + 1)]
        dp[0][0] = 0

        for i in range(size1):
            for mask in range(1 << size2):
                if dp[i][mask] == inf:
                    continue  # skip unreachable states

                # Try to connect current node i to each node j in group2
                for j in range(size2):
                    index1 = i + 1
                    index2 = mask | (1 << j)
                    cost_candidate = dp[i][mask] + cost[i][j]
                    if dp[index1][index2] > cost_candidate:
                        dp[index1][index2] = cost_candidate

                # Try to remove a previously connected j from mask to reduce cost
                for j in range(size2):
                    bit = 1 << j
                    if mask & bit != 0:
                        index1 = i + 1
                        cost_candidate = dp[index1][mask]
                        cost_reduce = dp[index1][mask ^ bit] + cost[i][j]
                        if cost_candidate > cost_reduce:
                            dp[index1][mask] = cost_reduce

        return dp[size1][(1 << size2) - 1]