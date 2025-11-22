class Solution:
    def integerBreak(self, n: int) -> int:
        dp = [0] * (n + 1)
        dp[1] = 1
        for i in range(2, n + 1):
            max_product = 0
            for j in range(1, i):
                max_product = max(max_product, j * dp[i - j], j * (i - j))
            dp[i] = max_product
        return dp[n]