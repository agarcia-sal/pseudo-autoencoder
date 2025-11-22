from typing import List

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m = len(word1)
        n = len(word2)
        # Initialize the dp table with zeros
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        # Base cases: converting empty string to prefix of other string
        for i in range(m + 1):
            dp[i][0] = i
        for j in range(n + 1):
            dp[0][j] = j

        # Compute dp values for each substring pair
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if word1[i - 1] == word2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = 1 + min(
                        dp[i - 1][j],    # deletion
                        dp[i][j - 1],    # insertion
                        dp[i - 1][j - 1] # substitution
                    )
        return dp[m][n]