class Solution:
    def numOfArrays(self, n: int, m: int, k: int) -> int:
        MOD = 10**9 + 7

        def initialize_dp():
            # dp dimensions: (n+1) x (m+1) x (k+1)
            return [[[0] * (k + 1) for _ in range(m + 1)] for __ in range(n + 1)]

        dp = initialize_dp()

        for j in range(1, m + 1):
            dp[1][j][1] = 1

        for i in range(2, n + 1):
            for j in range(1, m + 1):
                for p in range(1, k + 1):
                    # sum dp[i-1][x][p-1] for x in [1, j-1]
                    s = 0
                    for x in range(1, j):
                        s += dp[i - 1][x][p - 1]
                    s %= MOD

                    dp[i][j][p] = (s + dp[i - 1][j][p] * j) % MOD

        result = 0
        for j in range(1, m + 1):
            result = (result + dp[n][j][k]) % MOD

        return result