class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(1, m + 1):
            c1 = word1[i - 1]
            for j in range(1, n + 1):
                c2 = word2[j - 1]
                if c1 == c2:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
        lcs_length = dp[m][n]
        return m - lcs_length + n - lcs_length