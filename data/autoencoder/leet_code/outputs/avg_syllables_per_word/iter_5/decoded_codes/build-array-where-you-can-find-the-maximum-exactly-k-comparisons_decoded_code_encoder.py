class Solution:
    def numOfArrays(self, n: int, m: int, k: int) -> int:
        MOD = 10**9 + 7
        dp = [[[0] * (k + 1) for _ in range(m + 1)] for _ in range(n + 1)]

        for j in range(1, m + 1):
            dp[1][j][1] = 1

        for i in range(2, n + 1):
            for p in range(1, k + 1):
                prefix = 0
                for j in range(1, m + 1):
                    # sum dp[i-1][x][p-1] for x in [1..j-1]
                    if j > 1:
                        prefix = (prefix + dp[i-1][j-1][p-1]) % MOD
                    # dp[i][j][p] = prefix + dp[i-1][j][p] * j
                    dp[i][j][p] = (prefix + dp[i-1][j][p] * j) % MOD

        return sum(dp[n][j][k] for j in range(1, m + 1)) % MOD