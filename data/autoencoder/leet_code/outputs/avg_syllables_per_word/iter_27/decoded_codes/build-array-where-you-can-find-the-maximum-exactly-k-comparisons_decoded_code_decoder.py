from typing import List

class Solution:
    def numOfArrays(self, n: int, m: int, k: int) -> int:
        MOD = 10**9 + 7
        # dp[i][j][p]: number of arrays of length i,
        # with max element j,
        # and cost p
        dp = [[[0] * (k + 1) for _ in range(m + 1)] for __ in range(n + 1)]

        for j in range(1, m + 1):
            dp[1][j][1] = 1

        for i in range(2, n + 1):
            for j in range(1, m + 1):
                for p in range(1, k + 1):
                    # Arrays ending with max = j that were formed previously with smaller maxes
                    sum_smaller_max = 0
                    for x in range(1, j):
                        if p - 1 >= 0:
                            sum_smaller_max += dp[i - 1][x][p - 1]
                    dp[i][j][p] = (dp[i][j][p] + sum_smaller_max) % MOD

                    # Arrays where max stays j
                    dp[i][j][p] = (dp[i][j][p] + dp[i - 1][j][p] * j) % MOD

        result = 0
        for j in range(1, m + 1):
            result = (result + dp[n][j][k]) % MOD

        return result