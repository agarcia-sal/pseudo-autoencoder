class Solution:
    def isMatch(self, string_s: str, string_p: str) -> bool:
        m, n = len(string_s), len(string_p)
        dp = [[False] * (n + 1) for _ in range(m + 1)]
        dp[0][0] = True

        for j in range(1, n + 1):
            if string_p[j - 1] == '*':
                dp[0][j] = dp[0][j - 1]

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if string_p[j - 1] == '*':
                    dp[i][j] = dp[i - 1][j] or dp[i][j - 1]
                elif string_p[j - 1] == '?' or string_s[i - 1] == string_p[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]

        return dp[m][n]