from typing import List

class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        for s in strs:
            count_zero = s.count('0')
            count_one = s.count('1')
            for i in range(m, count_zero - 1, -1):
                for j in range(n, count_one - 1, -1):
                    dp[i][j] = max(dp[i][j], dp[i - count_zero][j - count_one] + 1)
        return dp[m][n]