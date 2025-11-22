from typing import List

class Solution:
    def dieSimulator(self, n: int, rollMax: List[int]) -> int:
        MOD = 10**9 + 7
        max_roll_max = max(rollMax)

        # dp[i][j][k]: number of sequences of length i with last die face j and k consecutive times rolled j
        dp = [[[0] * (max_roll_max + 1) for _ in range(6)] for _ in range(n + 1)]

        # Base case: for sequences of length 1, rolling each face once
        for j in range(6):
            dp[1][j][1] = 1

        for i in range(2, n + 1):
            for j in range(6):
                limit = rollMax[j]
                for k in range(1, limit + 1):
                    if k > 1:
                        dp[i][j][k] = dp[i - 1][j][k - 1]
                    else:
                        total = 0
                        for x in range(6):
                            if x != j:
                                total += sum(dp[i - 1][x][1:rollMax[x] + 1])
                        dp[i][j][1] = total % MOD
        result_sum = 0
        for j in range(6):
            result_sum += sum(dp[n][j][1:rollMax[j] + 1])
        return result_sum % MOD