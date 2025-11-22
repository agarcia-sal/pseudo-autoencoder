from typing import List

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m, n = len(s), len(p)
        # dp[i][j] means s[:i] matches p[:j]
        dp: List[List[bool]] = [[False] * (n + 1) for _ in range(m + 1)]
        dp[0][0] = True

        # Initialize dp for patterns like a*, a*b*, a*b*c* that can match empty string
        for j in range(1, n + 1):
            if p[j - 1] == '*':
                if j >= 2:
                    dp[0][j] = dp[0][j - 2]

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if p[j - 1] == s[i - 1] or p[j - 1] == '.':
                    dp[i][j] = dp[i - 1][j - 1]
                elif p[j - 1] == '*':
                    # '*' means zero occurrences of the char before '*'
                    dp[i][j] = dp[i][j - 2]
                    # if char before '*' matches current s char or char before '*' is '.'
                    if p[j - 2] == s[i - 1] or p[j - 2] == '.':
                        dp[i][j] = dp[i][j] or dp[i - 1][j]
        return dp[m][n]