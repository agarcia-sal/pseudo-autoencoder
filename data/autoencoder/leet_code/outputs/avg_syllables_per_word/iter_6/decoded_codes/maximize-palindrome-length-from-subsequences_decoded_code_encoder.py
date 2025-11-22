class Solution:
    def longestPalindrome(self, word1: str, word2: str) -> int:
        s = word1 + word2
        n = len(s)
        dp = [[0] * n for _ in range(n)]

        for i in range(n):
            dp[i][i] = 1

        max_len = 0
        split = len(word1)

        for length in range(2, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1
                if s[i] == s[j]:
                    dp[i][j] = (dp[i + 1][j - 1] if i + 1 <= j - 1 else 0) + 2
                    if i < split <= j and dp[i][j] > max_len:
                        max_len = dp[i][j]
                else:
                    dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])

        return max_len