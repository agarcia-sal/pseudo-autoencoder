class Solution:
    def matrixScore(self, grid):
        for row in grid:
            if row[0] == 0:
                for i in range(len(row)):
                    row[i] = 1 - row[i]

        rows, cols = len(grid), len(grid[0])
        for col in range(1, cols):
            count_ones = sum(grid[r][col] for r in range(rows))
            if count_ones < rows / 2:
                for r in range(rows):
                    grid[r][col] = 1 - grid[r][col]

        score = 0
        for row in grid:
            score += int("".join(map(str, row)), 2)

        return score