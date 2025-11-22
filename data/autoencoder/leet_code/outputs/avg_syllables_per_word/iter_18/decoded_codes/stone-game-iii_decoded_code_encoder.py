from typing import List

class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        n = len(stoneValue)
        dp = [0] * (n + 1)
        for i in range(n - 1, -1, -1):
            value_one = stoneValue[i]
            dp[i] = value_one - dp[i + 1]
            if i + 2 <= n:
                sum_two = stoneValue[i] + stoneValue[i + 1]
                dp[i] = max(dp[i], sum_two - dp[i + 2])
            if i + 3 <= n:
                sum_three = stoneValue[i] + stoneValue[i + 1] + stoneValue[i + 2]
                dp[i] = max(dp[i], sum_three - dp[i + 3])
        if dp[0] > 0:
            return "Alice"
        elif dp[0] < 0:
            return "Bob"
        else:
            return "Tie"