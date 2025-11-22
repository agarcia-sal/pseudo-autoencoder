class Solution:
    def longestPalindrome(self, word1, word2):
        s = word1 + word2
        n = len(s)
        dp = [[0] * n for _ in range(n)]

        for i in range(n):
            dp[i][i] = 1

        max_len = 0
        for length in range(2, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1
                if s[i] == s[j]:
                    dp[i][j] = dp[i + 1][j - 1] + 2 if i + 1 <= j - 1 else 2
                    if i < len(word1) and j >= len(word1):
                        max_len = max(max_len, dp[i][j])
                else:
                    dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])

        return max_len