class Solution:
    def numOfArrays(self, n, m, k):
        MOD = 10**9 + 7
        dp = [[[0] * (k + 1) for _ in range(m + 1)] for __ in range(n + 1)]

        for j in range(1, m + 1):
            dp[1][j][1] = 1

        for i in range(2, n + 1):
            for p in range(1, k + 1):
                prefix = [0] * (m + 1)
                for x in range(1, m + 1):
                    prefix[x] = (prefix[x-1] + dp[i - 1][x][p - 1]) % MOD

                for j in range(1, m + 1):
                    dp[i][j][p] = (prefix[j - 1] + dp[i - 1][j][p] * j) % MOD

        return sum(dp[n][j][k] for j in range(1, m + 1)) % MOD