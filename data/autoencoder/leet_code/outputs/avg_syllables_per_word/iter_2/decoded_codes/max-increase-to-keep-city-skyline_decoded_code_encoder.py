class Solution:
    def maxIncreaseKeepingSkyline(self, grid):
        n = len(grid)
        row_maxes = []
        for row in grid:
            row_maxes.append(max(row))

        col_maxes = []
        for col in zip(*grid):
            col_maxes.append(max(col))

        total_increase = 0
        for i in range(n):
            for j in range(n):
                max_height = min(row_maxes[i], col_maxes[j])
                total_increase += max(0, max_height - grid[i][j])

        return total_increase