class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        m, n = len(s1), len(s2)

        def createTwoDimensionalArray(rows: int, columns: int) -> list[list[int]]:
            return [[0] * columns for _ in range(rows)]

        dp = createTwoDimensionalArray(m + 1, n + 1)

        for j in range(1, n + 1):
            dp[0][j] = dp[0][j - 1] + ord(s2[j - 1])

        for i in range(1, m + 1):
            dp[i][0] = dp[i - 1][0] + ord(s1[i - 1])

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                char_s1 = s1[i - 1]
                char_s2 = s2[j - 1]
                if char_s1 == char_s2:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    value_delete_s1 = dp[i - 1][j] + ord(char_s1)
                    value_delete_s2 = dp[i][j - 1] + ord(char_s2)
                    dp[i][j] = min(value_delete_s1, value_delete_s2)

        return dp[m][n]