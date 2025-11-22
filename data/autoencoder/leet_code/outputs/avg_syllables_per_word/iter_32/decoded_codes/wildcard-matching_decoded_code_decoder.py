from typing import List

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        # dp[i][j] indicates whether s[:i] matches p[:j]
        dp: List[List[bool]] = [[False] * (len(p) + 1) for _ in range(len(s) + 1)]
        dp[0][0] = True  # empty pattern matches empty string

        # Initialize dp for patterns with '*' that can match empty string
        for j in range(1, len(p) + 1):
            if p[j - 1] == '*':
                dp[0][j] = dp[0][j - 1]

        for i in range(1, len(s) + 1):
            for j in range(1, len(p) + 1):
                if p[j - 1] == '*':
                    # '*' matches empty sequence (dp[i][j-1]) or one more character (dp[i-1][j])
                    dp[i][j] = dp[i][j - 1] or dp[i - 1][j]
                elif p[j - 1] == '?' or s[i - 1] == p[j - 1]:
                    # Match single character or '?'
                    dp[i][j] = dp[i - 1][j - 1]
                # else dp[i][j] remains False

        return dp[len(s)][len(p)]