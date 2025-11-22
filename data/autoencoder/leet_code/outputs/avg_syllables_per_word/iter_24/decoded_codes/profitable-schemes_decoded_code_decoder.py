class Solution:
    def profitableSchemes(self, n, profit_minimum, group, profit):
        MODULO = 10**9 + 7
        dp = [[0] * (profit_minimum + 1) for _ in range(n + 1)]
        for i in range(n + 1):
            dp[i][0] = 1
        for p, g in zip(profit, group):
            for i in range(n, g - 1, -1):
                for j in range(profit_minimum, -1, -1):
                    dp[i][j] += dp[i - g][max(0, j - p)]
                    dp[i][j] %= MODULO
        return dp[n][profit_minimum]