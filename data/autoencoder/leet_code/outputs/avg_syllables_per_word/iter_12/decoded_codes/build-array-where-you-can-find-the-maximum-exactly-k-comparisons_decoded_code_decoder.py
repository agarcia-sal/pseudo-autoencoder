class Solution:
    def numOfArrays(self, n: int, m: int, k: int) -> int:
        MOD = 10**9 + 7

        dp = self.initialize_dp_table(n, m, k)

        # Base case: For arrays of length 1, with max value j and exactly 1 search cost,
        # there's exactly one such array (the single element j).
        for j in range(1, m + 1):
            dp[1][j][1] = 1

        for i in range(2, n + 1):
            for j in range(1, m + 1):
                for p in range(1, k + 1):
                    # We sum over all x < j, adding ways where the max was x before,
                    # and now we pick j (which is bigger, so search cost increases by 1)
                    total = 0
                    for x in range(1, j):
                        total += dp[i - 1][x][p - 1]
                    total %= MOD

                    # Then add ways where max stays j (so last element <= j),
                    # and number of arrays dp[i-1][j][p], extend by any value <= j (which is j possibilities)
                    total += dp[i - 1][j][p] * j
                    total %= MOD

                    dp[i][j][p] = total

        result = 0
        for j in range(1, m + 1):
            result += dp[n][j][k]
            result %= MOD

        return result

    def initialize_dp_table(self, n: int, m: int, k: int):
        # dp dimensions: (n+1) x (m+1) x (k+1), filled with zeros
        return [[[0] * (k + 1) for _ in range(m + 1)] for __ in range(n + 1)]