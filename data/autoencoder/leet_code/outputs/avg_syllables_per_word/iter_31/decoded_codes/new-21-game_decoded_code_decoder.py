from typing import List

class Solution:
    def new21Game(self, n: int, k: int, maxPts: int) -> float:
        if k == 0 or n >= k + maxPts - 1:  # If k=0 or n is large enough, the probability is 1
            return 1.0

        dp: List[float] = [0.0] * (n + 1)
        dp[0] = 1.0
        window_sum = 1.0
        result = 0.0

        for i in range(1, n + 1):
            dp[i] = window_sum / maxPts
            if i < k:
                window_sum += dp[i]
            else:
                result += dp[i]
            if i - maxPts >= 0 and i - maxPts < k:
                window_sum -= dp[i - maxPts]

        return result