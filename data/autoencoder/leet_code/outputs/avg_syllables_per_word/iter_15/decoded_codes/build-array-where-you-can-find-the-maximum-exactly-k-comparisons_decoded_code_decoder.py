from typing import List

class Solution:
    def numOfArrays(self, n: int, m: int, k: int) -> int:
        MOD = 10**9 + 7

        # dp[i][j][p] represents the number of arrays of length i,
        # with maximum element j, and exactly p cost (number of times the max increased)
        dp = [[[0] * (k + 1) for _ in range(m + 1)] for __ in range(n + 1)]

        for j in range(1, m + 1):
            dp[1][j][1] = 1  # base case: arrays of length 1 with max j and cost 1

        for i in range(2, n + 1):
            for j in range(1, m + 1):
                for p in range(1, k + 1):
                    # sum over x < j, the max is increased by choosing a larger max j,
                    # thus cost p comes from p-1 before
                    s = 0
                    for x in range(1, j):
                        s += dp[i - 1][x][p - 1]
                    s %= MOD

                    # add arrays where max doesn't change
                    dp[i][j][p] = (s + dp[i - 1][j][p] * j) % MOD

        result = 0
        for j in range(1, m + 1):
            result = (result + dp[n][j][k]) % MOD

        return result