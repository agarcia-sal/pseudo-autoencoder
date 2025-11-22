class Solution:
    def matrixScore(self, grid):
        rows, cols = len(grid), len(grid[0])

        for row in grid:
            if row[0] == 0:
                for i in range(cols):
                    row[i] = 1 - row[i]

        for col in range(1, cols):
            count_ones = sum(grid[row][col] for row in range(rows))
            if count_ones < rows / 2:
                for row in range(rows):
                    grid[row][col] = 1 - grid[row][col]

        score = 0
        for row in grid:
            score += int(''.join(str(x) for x in row), 2)

        return score