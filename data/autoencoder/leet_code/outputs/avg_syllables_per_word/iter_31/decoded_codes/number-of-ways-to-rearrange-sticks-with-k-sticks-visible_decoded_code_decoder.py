from typing import List

class Solution:
    def rearrangeSticks(self, n: int, k: int) -> int:
        MOD = 10**9 + 1

        dp: List[List[int]] = [[0] * (k + 1) for _ in range(n + 1)]
        dp[0][0] = 1

        for i in range(1, n + 1):
            for j in range(1, k + 1):
                value_visible = dp[i - 1][j - 1]
                value_not_visible = (i - 1) * dp[i - 1][j]
                dp[i][j] = (value_visible + value_not_visible) % MOD

        return dp[n][k]