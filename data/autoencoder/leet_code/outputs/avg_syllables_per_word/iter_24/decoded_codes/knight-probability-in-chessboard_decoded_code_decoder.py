class Solution:
    def knightProbability(self, n, k, row, column):
        moves = [
            (-2, -1),
            (-2, 1),
            (-1, -2),
            (-1, 2),
            (1, -2),
            (1, 2),
            (2, -1),
            (2, 1),
        ]

        dp = [[0.0] * n for _ in range(n)]
        dp[row][column] = 1.0

        for _ in range(k):
            new_dp = [[0.0] * n for _ in range(n)]
            for r in range(n):
                for c in range(n):
                    if dp[r][c] != 0:
                        prob = dp[r][c] / 8.0
                        for dr, dc in moves:
                            nr, nc = r + dr, c + dc
                            if 0 <= nr < n and 0 <= nc < n:
                                new_dp[nr][nc] += prob
            dp = new_dp

        total_probability = 0.0
        for row_vals in dp:
            for val in row_vals:
                total_probability += val

        return total_probability