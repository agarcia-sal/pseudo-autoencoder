class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        n = len(s)
        dp = self.create_2D_array(n)

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

    def create_2d_array(self, n: int) -> list:
        dp = []
        for _ in range(n):
            dp.append([0] * n)
        return dp

    # Since the original pseudocode used create_2D_array, we implement it with exact name for compatibility
    create_2D_array = create_2d_array