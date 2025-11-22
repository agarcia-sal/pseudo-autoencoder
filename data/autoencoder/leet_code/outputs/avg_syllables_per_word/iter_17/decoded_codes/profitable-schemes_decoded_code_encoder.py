from typing import List

class Solution:
    def profitableSchemes(self, n: int, minProfit: int, group: List[int], profit: List[int]) -> int:
        MODULO = 10**9 + 7
        dp = [[0] * (minProfit + 1) for _ in range(n + 1)]
        for i in range(n + 1):
            dp[i][0] = 1
        for p, g in zip(profit, group):
            for members in range(n, g - 1, -1):
                for prof in range(minProfit, -1, -1):
                    prev_prof = max(0, prof - p)
                    dp[members][prof] = (dp[members][prof] + dp[members - g][prev_prof]) % MODULO
        return dp[n][minProfit]