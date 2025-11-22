from typing import List

class Solution:
    def profitableSchemes(self, n: int, profit_minimum: int, group: List[int], profit_list: List[int]) -> int:
        MOD = 10**9 + 7

        dp = [[0] * (profit_minimum + 1) for _ in range(n + 1)]
        for i in range(n + 1):
            dp[i][0] = 1

        for g, p in zip(group, profit_list):
            for i in range(n, g - 1, -1):
                for j in range(profit_minimum, -1, -1):
                    max_profit = max(0, j - p)
                    dp[i][j] = (dp[i][j] + dp[i - g][max_profit]) % MOD

        return dp[n][profit_minimum]