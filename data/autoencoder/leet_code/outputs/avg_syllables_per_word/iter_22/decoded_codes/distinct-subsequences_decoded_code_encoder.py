class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        m = len(s)
        n = len(t)

        # dp[i][j] will hold the number of distinct subsequences of s[:i] which equals t[:j]
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        # An empty string t can be matched by any prefix of s by deleting all characters
        for i in range(m + 1):
            dp[i][0] = 1

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if s[i - 1] == t[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j]
                else:
                    dp[i][j] = dp[i - 1][j]

        return dp[m][n]