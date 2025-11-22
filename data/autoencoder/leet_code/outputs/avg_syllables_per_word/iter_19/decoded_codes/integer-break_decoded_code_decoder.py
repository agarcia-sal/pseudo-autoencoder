class Solution:
    def integerBreak(self, n):
        dp = [0] * (n + 1)
        dp[1] = 1
        for i in range(2, n + 1):
            max_product = 0
            for j in range(1, i):
                product_one = j * dp[i - j]
                product_two = j * (i - j)
                max_product = max(max_product, product_one, product_two)
            dp[i] = max_product
        return dp[n]