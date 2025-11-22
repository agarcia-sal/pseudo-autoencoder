class Solution:
    def numOfArrays(self, n: int, m: int, k: int) -> int:
        MOD = 10**9 + 7
        # dp[i][j][p]: number of arrays of length i, max value j, exactly p array max changes
        dp = [[[0] * (k + 1) for _ in range(m + 1)] for __ in range(n + 1)]

        # Base case: for arrays of length 1, each number from 1 to m forms an array with max = number and 1 max change
        for j in range(1, m + 1):
            dp[1][j][1] = 1

        for i in range(2, n + 1):
            for j in range(1, m + 1):
                for p in range(1, k + 1):
                    # Sum dp[i-1][x][p-1] for x in [1, j-1]
                    s = 0
                    for x in range(1, j):
                        s += dp[i - 1][x][p - 1]
                    s %= MOD
                    dp[i][j][p] = (dp[i][j][p] + s) % MOD
                    # Add dp[i-1][j][p] * j (keep same max)
                    dp[i][j][p] = (dp[i][j][p] + dp[i - 1][j][p] * j) % MOD

        result = 0
        for j in range(1, m + 1):
            result = (result + dp[n][j][k]) % MOD
        return result