from typing import List, Optional

class Solution:
    def maximalSquare(self, matrix: Optional[List[List[str]]]) -> int:
        if not matrix or not matrix[0]:
            return 0

        m = len(matrix)
        n = len(matrix[0])
        dp = self.init_matrix(m + 1, n + 1)
        max_side = 0

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if matrix[i - 1][j - 1] == '1':
                    dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1
                    if dp[i][j] > max_side:
                        max_side = dp[i][j]

        return max_side * max_side

    def init_matrix(self, rows: int, columns: int) -> List[List[int]]:
        return [[0] * columns for _ in range(rows)]