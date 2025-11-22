class Solution:
    def maxIncreaseKeepingSkyline(self, grid):
        n = len(grid)
        row_maxes = [max(row) for row in grid]
        col_maxes = [max(col) for col in zip(*grid)]

        total_increase = 0
        for i in range(n):
            for j in range(n):
                max_height = min(row_maxes[i], col_maxes[j])
                increase = max(0, max_height - grid[i][j])
                total_increase += increase

        return total_increase