from typing import List

class Solution:
    def dieSimulator(self, n: int, rollMax: List[int]) -> int:
        MOD = 10**9 + 7
        max_roll = max(rollMax)
        # dp[i][j][k]: number of sequences of length i,
        # ending with face j (0-based),
        # with k consecutive appearances of face j
        dp = [[[0] * (max_roll + 1) for _ in range(6)] for _ in range(n + 1)]

        # Base case: sequences of length 1
        for j in range(6):
            dp[1][j][1] = 1

        for i in range(2, n + 1):
            for j in range(6):  # current face
                max_k = rollMax[j]
                for k in range(1, max_k + 1):
                    if k > 1:
                        # Extend sequence by repeating the same face j
                        dp[i][j][k] = dp[i - 1][j][k - 1]
                    else:
                        # k == 1, current face j is different from previous face
                        total = 0
                        for x in range(6):
                            if x != j:
                                max_x_k = rollMax[x]
                                for y in range(1, max_x_k + 1):
                                    total += dp[i - 1][x][y]
                        dp[i][j][k] = total % MOD

        result = 0
        for j in range(6):
            max_k = rollMax[j]
            for k in range(1, max_k + 1):
                result += dp[n][j][k]
        return result % MOD