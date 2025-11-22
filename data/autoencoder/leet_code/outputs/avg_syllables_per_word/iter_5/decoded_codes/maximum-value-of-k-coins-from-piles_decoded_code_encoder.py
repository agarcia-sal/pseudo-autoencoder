class Solution:
    def maxValueOfCoins(self, piles, k):
        n = len(piles)
        dp = [[0] * (k + 1) for _ in range(n + 1)]
        for i in range(1, n + 1):
            current_pile = piles[i - 1]
            prefix_sum = [0]
            for coin in current_pile:
                prefix_sum.append(prefix_sum[-1] + coin)
            for j in range(1, k + 1):
                dp[i][j] = dp[i - 1][j]
                for l in range(1, min(j, len(current_pile)) + 1):
                    dp[i][j] = max(dp[i][j], dp[i - 1][j - l] + prefix_sum[l])
        return dp[n][k]