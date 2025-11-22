class Solution:
    def new21Game(self, n: int, k: int, maxPts: int) -> float:
        if k == 0 or n >= k + maxPts:
            return 1.0

        dp = [0.0] * (n + maxPts + 1)
        for i in range(k, n + 1):
            dp[i] = 1.0

        window_sum = min(n - k + 1, maxPts)
        dp[k - 1] = window_sum / maxPts

        for i in range(k - 2, -1, -1):
            dp[i] = dp[i + 1] + (dp[i + 1] - dp[i + maxPts + 1]) / maxPts if (i + maxPts + 1) <= n + maxPts else dp[i + 1] + dp[i + 1] / maxPts

        return dp[0]