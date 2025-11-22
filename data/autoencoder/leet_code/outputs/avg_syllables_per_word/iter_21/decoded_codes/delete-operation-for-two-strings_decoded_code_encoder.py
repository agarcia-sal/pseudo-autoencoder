from typing import List

def createListOfZeros(length: int) -> List[int]:
    return [0] * length

def createTwoDimensionalArray(rows: int, columns: int) -> List[List[int]]:
    return [createListOfZeros(columns) for _ in range(rows)]

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m = len(word1)
        n = len(word2)
        dp = createTwoDimensionalArray(m + 1, n + 1)
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if word1[i - 1] == word2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
        lcs_length = dp[m][n]
        minimum_deletions = m - lcs_length + n - lcs_length
        return minimum_deletions