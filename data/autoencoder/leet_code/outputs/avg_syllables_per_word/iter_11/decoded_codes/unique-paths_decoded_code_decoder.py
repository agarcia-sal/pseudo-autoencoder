class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = self.createMatrix(m, n)
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
        return dp[m-1][n-1]

    def createMatrix(self, rows: int, columns: int) -> list[list[int]]:
        matrix = []
        for _ in range(rows):
            row = [1] * columns
            matrix.append(row)
        return matrix