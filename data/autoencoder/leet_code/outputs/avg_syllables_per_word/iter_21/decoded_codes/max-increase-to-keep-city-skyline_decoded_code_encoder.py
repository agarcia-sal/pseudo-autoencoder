class Solution:
    def maxIncreaseKeepingSkyline(self, grid):
        n = len(grid)
        row_maxes = self.get_row_maxes(grid)
        col_maxes = self.get_col_maxes(grid)
        total_increase = 0
        for i in range(n):
            for j in range(n):
                max_height = min(row_maxes[i], col_maxes[j])
                increase = max_height - grid[i][j]
                if increase > 0:
                    total_increase += increase
        return total_increase

    def get_row_maxes(self, grid):
        row_maxes = []
        for row in grid:
            current_max = float('-inf')
            for element in row:
                if element > current_max:
                    current_max = element
            row_maxes.append(current_max)
        return row_maxes

    def get_col_maxes(self, grid):
        n = len(grid)
        col_maxes = []
        for j in range(n):
            current_max = float('-inf')
            for i in range(n):
                if grid[i][j] > current_max:
                    current_max = grid[i][j]
            col_maxes.append(current_max)
        return col_maxes