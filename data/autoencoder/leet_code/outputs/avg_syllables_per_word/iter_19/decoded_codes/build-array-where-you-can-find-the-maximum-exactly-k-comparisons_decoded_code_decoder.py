class Solution:
    def numOfArrays(self, n, m, k):
        MOD = 10**9 + 7
        # dp[i][j][p]: number of arrays of length i, max value j, cost p
        dp = [[[0] * (k + 1) for _ in range(m + 1)] for __ in range(n + 1)]

        for j in range(1, m + 1):
            dp[1][j][1] = 1

        for i in range(2, n + 1):
            for p in range(1, k + 1):
                # prefix_sum[x]: sum of dp[i-1][x][p-1] for x in [1..j-1]
                prefix_sum = [0] * (m + 1)
                for x in range(1, m + 1):
                    prefix_sum[x] = (prefix_sum[x - 1] + dp[i - 1][x][p - 1]) % MOD

                for j in range(1, m + 1):
                    # Sum over x in [1..j-1] dp[i-1][x][p-1]
                    val = prefix_sum[j - 1] if j > 1 else 0
                    # Add arrays where max does not change: dp[i-1][j][p] * j
                    val = (val + dp[i - 1][j][p] * j) % MOD
                    dp[i][j][p] = val

        result = 0
        for j in range(1, m + 1):
            result = (result + dp[n][j][k]) % MOD
        return result