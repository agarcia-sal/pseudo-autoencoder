from typing import List

class Solution:
    def dieSimulator(self, n: int, rollMax: List[int]) -> int:
        MOD = 10**9 + 7
        max_roll = max(rollMax)
        # dp dimensions: (n+1) x 6 x (max_roll+1)
        # dp[i][j][k]: number of sequences of length i, ending with face j (0-based),
        # with j repeated k times consecutively
        dp = [[[0] * (rollMax[j] + 1) for j in range(6)] for _ in range(n + 1)]

        # Initialization: for sequences of length 1, each face j can appear once
        for j in range(6):
            dp[1][j][1] = 1

        for i in range(2, n + 1):
            for j in range(6):
                for k in range(1, rollMax[j] + 1):
                    if k > 1:
                        # If current face j is repeated k times, extend sequences that ended with j repeated k-1 times
                        dp[i][j][k] = dp[i - 1][j][k - 1]
                    else:
                        # If current face j starts a new sequence of this face,
                        # sum over sequences of length i-1 ending with any other face x
                        total = 0
                        for x in range(6):
                            if x != j:
                                total += sum(dp[i - 1][x][1 : rollMax[x] + 1])
                        dp[i][j][k] = total % MOD

        total_ways = 0
        for j in range(6):
            total_ways += sum(dp[n][j][1 : rollMax[j] + 1])
        return total_ways % MOD