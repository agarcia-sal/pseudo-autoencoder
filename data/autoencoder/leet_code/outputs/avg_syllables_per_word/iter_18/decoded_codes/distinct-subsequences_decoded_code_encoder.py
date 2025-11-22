class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        m, n = len(s), len(t)
        # Create a 2D dp array with (m+1) rows and (n+1) columns initialized to 0
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        # Every string s has exactly one subsequence matching the empty string t
        for i in range(m + 1):
            dp[i][0] = 1

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if s[i - 1] == t[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j]
                else:
                    dp[i][j] = dp[i - 1][j]

        return dp[m][n]