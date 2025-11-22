from math import inf

class Solution:
    def connectTwoGroups(self, cost):
        size1 = len(cost)
        size2 = len(cost[0])
        dp = [[inf] * (1 << size2) for _ in range(size1 + 1)]
        dp[0][0] = 0

        for i in range(size1):
            for mask in range(1 << size2):
                prev_val = dp[i][mask]
                if prev_val == inf:
                    continue
                for j in range(size2):
                    combined_mask = mask | (1 << j)
                    candidate_value = prev_val + cost[i][j]
                    if candidate_value < dp[i + 1][combined_mask]:
                        dp[i + 1][combined_mask] = candidate_value

                for j in range(size2):
                    bit_mask = 1 << j
                    if (bit_mask & mask) != 0:
                        without_bit_mask = mask & (~bit_mask)
                        alternative_value = dp[i + 1][without_bit_mask] + cost[i][j]
                        if alternative_value < dp[i + 1][mask]:
                            dp[i + 1][mask] = alternative_value

        full_mask = (1 << size2) - 1
        return dp[size1][full_mask]