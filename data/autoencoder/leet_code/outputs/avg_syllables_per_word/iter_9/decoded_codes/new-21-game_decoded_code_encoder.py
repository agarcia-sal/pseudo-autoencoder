class Solution:
    def new21Game(self, n: int, k: int, maxPts: int) -> float:
        if k == 0 or n >= k - 1 + maxPts:
            return 1.0

        dp = [0.0] * (n + maxPts + 1)
        for i in range(k, n + 1):
            dp[i] = 1.0

        window_sum = sum(dp[k:k + maxPts])
        for i in range(k - 1, -1, -1):
            dp[i] = window_sum / maxPts
            window_sum += dp[i] - dp[i + maxPts]

        return dp[0]