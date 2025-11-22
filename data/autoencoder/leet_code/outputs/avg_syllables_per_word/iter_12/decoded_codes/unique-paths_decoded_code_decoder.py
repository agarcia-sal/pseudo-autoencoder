class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = self.create_two_dimensional_list_with_value(1, m, n)
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
        return dp[m - 1][n - 1]

    def create_two_dimensional_list_with_value(self, value: int, rows: int, columns: int) -> list[list[int]]:
        return [[value for _ in range(columns)] for _ in range(rows)]