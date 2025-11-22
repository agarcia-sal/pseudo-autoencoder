from typing import List

class Solution:
    def dieSimulator(self, n: int, rollMax: List[int]) -> int:
        MOD = 10**9 + 7

        dp = self.initialize_dp(n, rollMax)

        # Base case initialization: for i=1, each face can appear once
        for j in range(6):
            dp[1][j][1] = 1

        for i in range(2, n + 1):
            for j in range(6):  # current face
                for k in range(1, rollMax[j] + 1):  # current consecutive count
                    if k > 1:
                        # continue rolling the same face j; consecutive count k depends on previous k-1 at position i-1
                        dp[i][j][k] = dp[i - 1][j][k - 1]
                    else:
                        # k == 1 means this face j just appeared after a different face
                        total_sum = 0
                        for x in range(6):
                            if x != j:
                                for y in range(1, rollMax[x] + 1):
                                    total_sum += dp[i - 1][x][y]
                        dp[i][j][k] = total_sum % MOD

        final_sum = 0
        for j in range(6):
            for k in range(1, rollMax[j] + 1):
                final_sum += dp[n][j][k]

        return final_sum % MOD

    def initialize_dp(self, n: int, rollMax: List[int]) -> List[List[List[int]]]:
        max_roll = max(rollMax)
        # dp dimension: (n+1) x 6 x (max_roll+1)
        # dp[i][j][k]: number of sequences of length i,
        # ending with face j (0-based), with k consecutive appearances of j
        return [[[0] * (max_roll + 1) for _ in range(6)] for _ in range(n + 1)]