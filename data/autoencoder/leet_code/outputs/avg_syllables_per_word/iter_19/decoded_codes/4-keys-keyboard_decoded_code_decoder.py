class Solution:
    def maxA(self, n):
        if n <= 3:
            return n

        dp = [0] * (n + 1)
        for i in range(1, 4):
            dp[i] = i

        for i in range(4, n + 1):
            for j in range(i - 3, 0, -1):
                possible_value = dp[j] * (i - j - 1)
                if possible_value > dp[i]:
                    dp[i] = possible_value

        return dp[n]