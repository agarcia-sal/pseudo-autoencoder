class Solution:
    def integerBreak(self, n: int) -> int:
        dp = [0] * (n + 1)
        dp[1] = 1
        for i in range(2, n + 1):
            max_product = 0
            for j in range(1, i):
                candidate_two = j * dp[i - j]
                candidate_three = j * (i - j)
                max_product = max(max_product, candidate_two, candidate_three)
            dp[i] = max_product
        return dp[n]