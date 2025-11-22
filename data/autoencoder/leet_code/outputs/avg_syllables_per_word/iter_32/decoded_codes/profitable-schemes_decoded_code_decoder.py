from typing import List

class Solution:
    def profitableSchemes(self, n: int, minProfit: int, group: List[int], profit: List[int]) -> int:
        MODULO = 10 ** 9 + 7
        # dp[i][j] = number of schemes using i members achieving at least j profit
        dp = [[0] * (minProfit + 1) for _ in range(n + 1)]
        for i in range(n + 1):
            dp[i][0] = 1  # zero profit always achievable by choosing no crimes

        for g, p in zip(group, profit):
            # iterate in reverse to avoid using updated states prematurely
            for i in range(n, g - 1, -1):
                for j in range(minProfit, -1, -1):
                    dp[i][j] = (dp[i][j] + dp[i - g][max(0, j - p)]) % MODULO

        return dp[n][minProfit]