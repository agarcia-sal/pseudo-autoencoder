class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m = len(word1)
        n = len(word2)
        dp = self.createTwoDimensionalArray(m + 1, n + 1)
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if word1[i - 1] == word2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
        lcs_length = dp[m][n]
        return m - lcs_length + n - lcs_length

    def createTwoDimensionalArray(self, rows: int, columns: int) -> list[list[int]]:
        array = []
        for _ in range(rows):
            array.append([0] * columns)
        return array