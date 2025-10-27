class Solution:
    def numOfArrays(self, n: int, m: int, k: int) -> int:
        MOD = 10**9 + 7

        # dp[i][j][p]: number of arrays of length i,
        # with max element j, and exactly p comparisons
        dp = [[[0] * (k + 1) for _ in range(m + 1)] for __ in range(n + 1)]

        for j in range(1, m + 1):
            dp[1][j][1] = 1

        for i in range(2, n + 1):
            for j in range(1, m + 1):
                for p in range(1, k + 1):
                    # sum of dp[i-1][x][p-1] for x in [1..j-1]
                    # use direct summation as in pseudocode
                    total = 0
                    for x in range(1, j):
                        total += dp[i - 1][x][p - 1]
                    total %= MOD

                    dp[i][j][p] = (dp[i][j][p] + total) % MOD
                    dp[i][j][p] = (dp[i][j][p] + dp[i - 1][j][p] * j) % MOD

        result = 0
        for j in range(1, m + 1):
            result = (result + dp[n][j][k]) % MOD

        return result