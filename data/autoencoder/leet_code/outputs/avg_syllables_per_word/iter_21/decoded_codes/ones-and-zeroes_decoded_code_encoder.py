from typing import List

class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        # Helper to create a 2D array initialized with a specific value
        def createTwoDimensionalArray(rows: int, cols: int, val: int) -> List[List[int]]:
            return [[val] * cols for _ in range(rows)]

        # Helper to count occurrences of a character in a string
        def countCharacterOccurrences(s: str, ch: str) -> int:
            return s.count(ch)

        # Helper to get maximum of two values
        def getMaximum(a: int, b: int) -> int:
            return max(a, b)

        dp = createTwoDimensionalArray(m + 1, n + 1, 0)
        zeroCharacter = '0'
        oneCharacter = '1'

        for s in strs:
            count_0 = countCharacterOccurrences(s, zeroCharacter)
            count_1 = countCharacterOccurrences(s, oneCharacter)
            for i in range(m, count_0 - 1, -1):
                for j in range(n, count_1 - 1, -1):
                    dp[i][j] = getMaximum(dp[i][j], dp[i - count_0][j - count_1] + 1)

        return dp[m][n]