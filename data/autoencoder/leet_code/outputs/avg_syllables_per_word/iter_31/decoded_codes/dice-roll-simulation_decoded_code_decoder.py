from typing import List

class Solution:
    def dieSimulator(self, n: int, rollMax: List[int]) -> int:
        MOD = 10**9 + 7
        max_roll = max(rollMax)
        # dp[i][j][k]: number of ways to have length i,
        # ending with face j (0-based),
        # with k consecutive rolls of face j
        dp = [[[0] * (rollMax[j] + 1) for j in range(6)] for _ in range(n + 1)]

        # Initialization: for sequences of length 1,
        # each face can appear once consecutively
        for j in range(6):
            dp[1][j][1] = 1

        for i in range(2, n + 1):
            for j in range(6):
                max_k = rollMax[j]
                for k in range(1, max_k + 1):
                    if k > 1:
                        dp[i][j][k] = dp[i - 1][j][k - 1]
                    else:
                        # Sum over all faces different from j and all valid consecutive counts
                        temp_sum = 0
                        for x in range(6):
                            if x != j:
                                max_x = rollMax[x]
                                temp_sum += sum(dp[i - 1][x][1 : max_x + 1])
                        dp[i][j][k] = temp_sum % MOD

        total_ways = 0
        for j in range(6):
            total_ways += sum(dp[n][j][1 : rollMax[j] + 1])
        return total_ways % MOD