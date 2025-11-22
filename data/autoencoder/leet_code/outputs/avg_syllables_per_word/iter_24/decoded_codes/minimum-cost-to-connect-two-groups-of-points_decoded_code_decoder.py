from math import inf

class Solution:
    def connectTwoGroups(self, cost):
        size1 = len(cost)
        size2 = len(cost[0])
        dp = [[inf] * (1 << size2) for _ in range(size1 + 1)]
        dp[0][0] = 0

        for i in range(size1):
            for mask in range(1 << size2):
                for j in range(size2):
                    index1 = i + 1
                    index2 = mask | (1 << j)
                    current_value = dp[index1][index2]
                    new_value = dp[i][mask] + cost[i][j]
                    if new_value < current_value:
                        dp[index1][index2] = new_value

                for j in range(size2):
                    if (mask & (1 << j)) != 0:
                        index1 = i + 1
                        index2 = mask
                        index3 = mask ^ (1 << j)
                        current_value = dp[index1][index2]
                        new_value = dp[index1][index3] + cost[i][j]
                        if new_value < current_value:
                            dp[index1][index2] = new_value

        final_mask = (1 << size2) - 1
        return dp[size1][final_mask]