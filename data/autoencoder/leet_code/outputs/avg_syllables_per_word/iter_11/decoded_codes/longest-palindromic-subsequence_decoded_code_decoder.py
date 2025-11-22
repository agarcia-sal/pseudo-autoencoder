class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        n = len(s)
        dp = self.initialize_dp(n)
        for i in range(n):
            dp[i][i] = 1
        for length in range(2, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1
                if s[i] == s[j]:
                    dp[i][j] = dp[i + 1][j - 1] + 2
                else:
                    dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])
        return dp[0][n - 1]

    def initialize_dp(self, n: int) -> list[list[int]]:
        return [[0] * n for _ in range(n)]