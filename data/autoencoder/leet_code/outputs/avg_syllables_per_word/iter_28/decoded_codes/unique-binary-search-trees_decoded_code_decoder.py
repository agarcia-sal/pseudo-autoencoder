from typing import List

class Solution:
    def numTrees(self, n: int) -> int:
        dp: List[int] = [0] * (n + 1)
        dp[0] = 1
        if n >= 1:
            dp[1] = 1
        for i in range(2, n + 1):
            for j in range(1, i + 1):
                dp[i] += dp[j - 1] * dp[i - j]
        return dp[n]