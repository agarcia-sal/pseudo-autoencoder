from typing import List

class Solution:
    def integerBreak(self, n: int) -> int:
        dp: List[int] = [0] * (n + 1)
        dp[1] = 1
        for i in range(2, n + 1):
            max_product = 0
            for j in range(1, i):
                product_one = j * dp[i - j]
                product_two = j * (i - j)
                if max_product < product_one and max_product < product_two:
                    max_product = max(product_one, product_two, max_product)
                elif max_product < product_one:
                    max_product = product_one
                elif max_product < product_two:
                    max_product = product_two
            dp[i] = max_product
        return dp[n]