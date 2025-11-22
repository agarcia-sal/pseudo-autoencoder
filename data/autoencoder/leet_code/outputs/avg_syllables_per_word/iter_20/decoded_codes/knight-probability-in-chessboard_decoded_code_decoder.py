class Solution:
    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:
        moves = [(-2, -1), (-2, 1), (-1, -2), (-1, 2),
                 (1, -2), (1, 2), (2, -1), (2, 1)]

        dp = [[0.0] * n for _ in range(n)]
        dp[row][column] = 1.0

        for _ in range(k):
            new_dp = [[0.0] * n for _ in range(n)]
            for r in range(n):
                for c in range(n):
                    prob = dp[r][c]
                    if prob == 0:
                        continue
                    share = prob / 8.0
                    for dr, dc in moves:
                        nr, nc = r + dr, c + dc
                        if 0 <= nr < n and 0 <= nc < n:
                            new_dp[nr][nc] += share
            dp = new_dp

        total_probability = 0.0
        for inner_row in dp:
            for val in inner_row:
                total_probability += val

        return total_probability