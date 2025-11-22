class Solution:
    def stoneGameIII(self, stoneValue):
        n = len(stoneValue)
        dp = [0] * (n + 1)

        for index in range(n - 1, -1, -1):
            dp[index] = stoneValue[index] - dp[index + 1]
            if index + 2 <= n:
                dp[index] = max(dp[index], stoneValue[index] + stoneValue[index + 1] - dp[index + 2])
            if index + 3 <= n:
                dp[index] = max(dp[index], stoneValue[index] + stoneValue[index + 1] + stoneValue[index + 2] - dp[index + 3])

        if dp[0] > 0:
            return "Alice"
        elif dp[0] < 0:
            return "Bob"
        else:
            return "Tie"