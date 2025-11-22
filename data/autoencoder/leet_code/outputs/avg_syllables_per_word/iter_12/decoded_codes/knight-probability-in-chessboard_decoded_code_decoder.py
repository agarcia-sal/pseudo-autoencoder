class Solution:
    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:
        moves = [(-2, -1), (-2, 1), (-1, -2), (-1, 2),
                 (1, -2), (1, 2), (2, -1), (2, 1)]

        dp = self.initialize_dp_table(n)
        dp[row][column] = 1.0

        for _ in range(k):
            new_dp = self.initialize_dp_table(n)
            for r in range(n):
                for c in range(n):
                    if dp[r][c] == 0:
                        continue
                    prob = dp[r][c] / 8
                    for dr, dc in moves:
                        nr, nc = r + dr, c + dc
                        if 0 <= nr < n and 0 <= nc < n:
                            new_dp[nr][nc] += prob
            dp = new_dp

        total_probability = 0.0
        for dp_row in dp:
            for value in dp_row:
                total_probability += value

        return total_probability

    def initialize_dp_table(self, n: int) -> list[list[float]]:
        return [[0.0] * n for _ in range(n)]