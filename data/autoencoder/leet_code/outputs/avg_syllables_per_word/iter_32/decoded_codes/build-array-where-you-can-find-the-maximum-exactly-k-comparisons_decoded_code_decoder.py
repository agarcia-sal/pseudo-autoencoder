from typing import List

class Solution:
    def numOfArrays(self, n: int, m: int, k: int) -> int:
        MOD = 10**9 + 7

        # dp[i][j][p] = number of arrays of length i, max element j, with cost p
        # Dimensions: (n+1) x (m+1) x (k+1)
        dp = [[[0] * (k + 1) for _ in range(m + 1)] for __ in range(n + 1)]

        # Initialization: arrays of length 1 with max element j and cost=1 are 1
        for j in range(1, m + 1):
            dp[1][j][1] = 1

        for i in range(2, n + 1):
            for j in range(1, m + 1):
                for p in range(1, k + 1):
                    # Add sequences where current max element is j and cost is p, 
                    # and last element is less than j - which increases cost by 1,
                    # so previous cost must be p-1
                    if p > 1:
                        for x in range(1, j):
                            dp[i][j][p] += dp[i-1][x][p-1]
                            if dp[i][j][p] >= MOD:
                                dp[i][j][p] %= MOD
                    # Add sequences where current max element remains j
                    # Multiply by j because last element can be any among 1..j (and to keep max=j doesn't increase cost)
                    dp[i][j][p] += dp[i-1][j][p] * j
                    dp[i][j][p] %= MOD

        result = 0
        for j in range(1, m + 1):
            result += dp[n][j][k]
            if result >= MOD:
                result %= MOD

        return result