class Solution:
    def numOfArrays(self, n: int, m: int, k: int) -> int:
        MOD = 10**9 + 7

        # dp[i][j][p] means:
        # Number of arrays of length i,
        # with maximum value j,
        # and exactly p new maximums.
        # Dimensions: (n+1) x (m+1) x (k+1)
        dp = [[[0] * (k + 1) for _ in range(m + 1)] for _ in range(n + 1)]

        # Base case: for arrays of length 1,
        # every element j (1 <= j <= m) forms an array with 1 new maximum
        for j in range(1, m + 1):
            dp[1][j][1] = 1

        for i in range(2, n + 1):
            for j in range(1, m + 1):
                for p in range(1, k + 1):
                    # Append an element which is less than current max j
                    # Means new max count 'p-1' for the previous array of length i-1
                    total = 0
                    for x in range(1, j):
                        total += dp[i - 1][x][p - 1]
                    dp[i][j][p] = total % MOD

                    # Append an element equal to current max j
                    # The number of ways previous array has max j count p
                    # The new element can be any of j values equal to max j
                    dp[i][j][p] += dp[i - 1][j][p] * j
                    dp[i][j][p] %= MOD

        result = 0
        for j in range(1, m + 1):
            result += dp[n][j][k]
        result %= MOD

        return result