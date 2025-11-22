from typing import List

class Solution:
    def profitableSchemes(self, n: int, minProfit: int, group: List[int], profit: List[int]) -> int:
        MOD = 10**9 + 7
        # dp[i][j] = number of schemes using at most i members with at least j profit (capped at minProfit)
        dp = [[0] * (minProfit + 1) for _ in range(n + 1)]

        # There is always 1 way to have 0 profit with 0 members (do nothing)
        for i in range(n + 1):
            dp[i][0] = 1

        for p, g in zip(profit, group):
            for i in range(n, g - 1, -1):
                for j in range(minProfit, -1, -1):
                    prev_profit_idx = max(0, j - p)
                    dp[i][j] = (dp[i][j] + dp[i - g][prev_profit_idx]) % MOD

        return dp[n][minProfit]