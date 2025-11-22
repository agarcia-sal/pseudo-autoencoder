from typing import List

class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        m, n = len(s1), len(s2)
        # dp[i][j] will hold the minimum ASCII delete sum to make s1[:i] and s2[:j] equal
        dp: List[List[int]] = [[0] * (n + 1) for _ in range(m + 1)]

        # Initialize first row (s1 is empty, delete all chars of s2)
        for j in range(1, n + 1):
            dp[0][j] = dp[0][j - 1] + ord(s2[j - 1])

        # Initialize first column (s2 is empty, delete all chars of s1)
        for i in range(1, m + 1):
            dp[i][0] = dp[i - 1][0] + ord(s1[i - 1])

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if s1[i - 1] == s2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = min(
                        dp[i - 1][j] + ord(s1[i - 1]),
                        dp[i][j - 1] + ord(s2[j - 1])
                    )
        return dp[m][n]