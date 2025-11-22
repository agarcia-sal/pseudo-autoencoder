class Solution:
    def numOfArrays(self, n: int, m: int, k: int) -> int:
        MOD = 10**9 + 7
        # dp[i][j][p]: number of arrays of length i, max element exactly j, with p changes in max
        # Using dimensions (n+1) x (m+1) x (k+1) initialized to 0
        dp = [[[0] * (k + 1) for _ in range(m + 1)] for __ in range(n + 1)]

        # Base case: length 1 arrays, max j, with 1 max-change = 1
        for j in range(1, m + 1):
            dp[1][j][1] = 1

        for i in range(2, n + 1):
            for j in range(1, m + 1):
                for p in range(1, k + 1):
                    # Add arrays where max changed to j at position i:
                    # sum dp[i-1][x][p-1] for x in [1, j-1]
                    s = 0
                    for x in range(1, j):
                        s += dp[i - 1][x][p - 1]
                    s %= MOD

                    # Add arrays where max remains j:
                    # dp[i-1][j][p] * j
                    s += dp[i - 1][j][p] * j
                    s %= MOD

                    dp[i][j][p] = s

        result = 0
        for j in range(1, m + 1):
            result += dp[n][j][k]
        return result % MOD