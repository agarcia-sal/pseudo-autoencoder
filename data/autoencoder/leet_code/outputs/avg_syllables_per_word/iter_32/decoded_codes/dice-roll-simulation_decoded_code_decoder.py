from typing import List

class Solution:
    def dieSimulator(self, n: int, rollMax: List[int]) -> int:
        MOD = 10**9 + 7
        max_roll = max(rollMax)
        # dp[i][j][k]: number of sequences of length i, ending with number j, repeated k times consecutively
        dp = [[[0] * (rollMax[j] + 1) for j in range(6)] for _ in range(n + 1)]

        # Initialization for sequences of length 1
        for j in range(6):
            dp[1][j][1] = 1

        for i in range(2, n + 1):
            for j in range(6):
                for k in range(1, rollMax[j] + 1):
                    if k > 1:
                        # Continue the same number j
                        dp[i][j][k] = dp[i - 1][j][k - 1] % MOD
                    else:
                        # Start new number j after different number
                        sum_value = 0
                        for x in range(6):
                            if x != j:
                                sum_value += sum(dp[i - 1][x][1:rollMax[x] + 1])
                        dp[i][j][1] = sum_value % MOD

        result_sum = 0
        for j in range(6):
            result_sum += sum(dp[n][j][1:rollMax[j] + 1])
        return result_sum % MOD