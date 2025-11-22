from typing import List

class Solution:
    def numOfArrays(self, n: int, m: int, k: int) -> int:
        MOD = 10**9 + 7
        # dp[i][j][p] = number of arrays of length i, with max element j, and cost p
        dp = [[[0] * (k + 1) for _ in range(m + 1)] for __ in range(n + 1)]

        # Initialization: arrays of length 1 have cost 1 and max element j
        for j in range(1, m + 1):
            dp[1][j][1] = 1

        for i in range(2, n + 1):
            for j in range(1, m + 1):
                for p in range(1, k + 1):
                    # Adding an element that does not increase max (<= j)
                    dp[i][j][p] += dp[i - 1][j][p] * j
                    dp[i][j][p] %= MOD

                    # Adding an element that increases max (from x < j to j)
                    if p > 1:
                        # sum dp[i-1][x][p-1] for x in [1..j-1]
                        # To optimize from O(m) inside triple loop, precompute prefix sums:
                        # But since code only directly requested translation preserving structure,
                        # Either do prefix sums here or do plain loop
                        # However, a nested loop over m upto 100 makes it okay for Python here.
                        total = 0
                        for x in range(1, j):
                            total += dp[i - 1][x][p - 1]
                        dp[i][j][p] += total
                        dp[i][j][p] %= MOD

        result = 0
        for j in range(1, m + 1):
            result += dp[n][j][k]
            result %= MOD

        return result