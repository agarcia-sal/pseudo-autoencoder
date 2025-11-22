class Solution:
    def matrixScore(self, grid):
        m, n = len(grid), len(grid[0])

        for row in grid:
            if row[0] == 0:
                for i in range(n):
                    row[i] = 1 - row[i]

        for col in range(1, n):
            count_ones = sum(grid[row][col] for row in range(m))
            if count_ones < m / 2:
                for row in range(m):
                    grid[row][col] = 1 - grid[row][col]

        score = 0
        for row in grid:
            score += int("".join(str(v) for v in row), 2)

        return score