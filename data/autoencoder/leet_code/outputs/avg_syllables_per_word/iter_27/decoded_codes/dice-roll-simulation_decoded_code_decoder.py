from typing import List

class Solution:
    def dieSimulator(self, n: int, rollMax: List[int]) -> int:
        MOD = 10**9 + 7
        max_roll = max(rollMax)
        # dp[i][j][k]: number of sequences of length i, ending with face j (0-based), 
        # with k consecutive rolls of face j
        dp = [[[0] * (max_roll + 1) for _ in range(6)] for _ in range(n + 1)]

        # Initialize for sequences of length 1
        for j in range(6):
            dp[1][j][1] = 1

        for i in range(2, n + 1):
            for j in range(6):
                max_consec = rollMax[j]
                for k in range(1, max_consec + 1):
                    if k > 1:
                        # Continuing with the same face j
                        dp[i][j][k] = dp[i-1][j][k-1] % MOD
                    else:
                        # k == 1, means the previous roll was a different face
                        temp_sum = 0
                        for x in range(6):
                            if x != j:
                                for y in range(1, rollMax[x] + 1):
                                    temp_sum += dp[i-1][x][y]
                        dp[i][j][k] = temp_sum % MOD

        result_sum = 0
        for j in range(6):
            for k in range(1, rollMax[j] + 1):
                result_sum += dp[n][j][k]

        return result_sum % MOD