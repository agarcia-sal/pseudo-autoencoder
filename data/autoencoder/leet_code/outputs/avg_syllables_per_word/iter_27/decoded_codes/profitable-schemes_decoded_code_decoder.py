from typing import List

class Solution:
    def profitableSchemes(self, n: int, minProfit: int, group: List[int], profit: List[int]) -> int:
        MOD = 10**9 + 7
        dp = [[0] * (minProfit + 1) for _ in range(n + 1)]
        for i in range(n + 1):
            dp[i][0] = 1
        for p, g in zip(profit, group):
            for i in range(n, g - 1, -1):
                for j in range(minProfit, -1, -1):
                    dp[i][j] = (dp[i][j] + dp[i - g][max(0, j - p)]) % MOD
        return dp[n][minProfit]