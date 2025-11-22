class Solution:
    def maxA(self, n: int) -> int:
        if n <= 3:
            return n

        dp = [0] * (n + 1)
        for i in range(1, 4):
            dp[i] = i

        for i in range(4, n + 1):
            for j in range(i - 3, 0, -1):
                product = dp[j] * (i - j - 1)
                if product > dp[i]:
                    dp[i] = product

        return dp[n]