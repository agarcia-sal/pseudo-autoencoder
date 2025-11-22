from typing import List

class Solution:
    def numTrees(self, n: int) -> int:
        if n <= 1:
            return 1
        dp: List[int] = [0] * (n + 1)
        dp[0], dp[1] = 1, 1
        for i in range(2, n + 1):
            total = 0
            for j in range(1, i + 1):
                total += dp[j - 1] * dp[i - j]
            dp[i] = total
        return dp[n]