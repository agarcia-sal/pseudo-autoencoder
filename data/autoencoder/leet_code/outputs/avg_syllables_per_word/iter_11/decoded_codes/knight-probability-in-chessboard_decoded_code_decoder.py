class Solution:
    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:
        moves = [(-2, -1), (-2, 1), (-1, -2), (-1, 2),
                 (1, -2), (1, 2), (2, -1), (2, 1)]

        dp = self.initialize_matrix(n, n)
        dp[row][column] = 1.0

        for _ in range(k):
            new_dp = self.initialize_matrix(n, n)
            for r in range(n):
                for c in range(n):
                    if dp[r][c] == 0:
                        continue
                    for dr, dc in moves:
                        nr, nc = r + dr, c + dc
                        if 0 <= nr < n and 0 <= nc < n:
                            new_dp[nr][nc] += dp[r][c] / 8
            dp = new_dp

        total_probability = 0.0
        for row_list in dp:
            for probability_value in row_list:
                total_probability += probability_value

        return total_probability

    def initialize_matrix(self, rows: int, columns: int) -> list:
        matrix = []
        for _ in range(rows):
            row_list = []
            for _ in range(columns):
                row_list.append(0)
            matrix.append(row_list)
        return matrix