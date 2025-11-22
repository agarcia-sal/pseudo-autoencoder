from typing import List

class Solution:
    def integerBreak(self, n: int) -> int:
        dp: List[int] = [0] * (n + 1)
        dp[1] = 1
        for i in range(2, n + 1):
            max_product = 0
            for j in range(1, i):
                candidate1 = j * dp[i - j]
                candidate2 = j * (i - j)
                max_product = max(max_product, candidate1, candidate2)
            dp[i] = max_product
        return dp[n]