class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        m = len(s1)
        n = len(s2)

        dp = self.construct_2D_list(m + 1, n + 1)

        for j in range(1, n + 1):
            dp[0][j] = dp[0][j - 1] + ord(s2[j - 1])

        for i in range(1, m + 1):
            dp[i][0] = dp[i - 1][0] + ord(s1[i - 1])

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if s1[i - 1] == s2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = min(
                        dp[i - 1][j] + ord(s1[i - 1]),
                        dp[i][j - 1] + ord(s2[j - 1])
                    )

        return dp[m][n]

    def construct_2D_list(self, rows: int, columns: int) -> list[list[int]]:
        return [[0] * columns for _ in range(rows)]