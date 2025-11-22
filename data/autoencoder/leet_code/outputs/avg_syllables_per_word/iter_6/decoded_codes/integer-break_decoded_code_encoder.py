class Solution:
    def integerBreak(self, n: int) -> int:
        dp = [0] * (n + 1)
        dp[1] = 1

        for i in range(2, n + 1):
            max_product = 0
            for j in range(1, i):
                product_option_1 = j * dp[i - j]
                product_option_2 = j * (i - j)
                max_product = max(max_product, product_option_1, product_option_2)
            dp[i] = max_product

        return dp[n]