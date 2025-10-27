class Solution:
    def profitableSchemes(self, n: int, profit_minimum: int, group: list[int], profit: list[int]) -> int:
        constant_mod = 10**9 + 7
        dp = [[0] * (profit_minimum + 1) for _ in range(n + 1)]
        for i in range(n + 1):
            dp[i][0] = 1  # Base case: zero profit is always achievable

        for p, g in zip(profit, group):
            for i in range(n, g - 1, -1):
                for j in range(profit_minimum, -1, -1):
                    j_minus_p = j - p
                    if j_minus_p < 0:
                        j_minus_p = 0
                    dp[i][j] = (dp[i][j] + dp[i - g][j_minus_p]) % constant_mod

        return dp[n][profit_minimum]