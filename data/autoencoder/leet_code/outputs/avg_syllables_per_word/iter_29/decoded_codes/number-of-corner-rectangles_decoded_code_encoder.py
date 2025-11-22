class Solution:
    def countCornerRectangles(self, grid):
        if not grid or not grid[0]:
            return 0

        m, n = len(grid), len(grid[0])
        count = 0

        for i in range(m):
            for j in range(i + 1, m):
                cols_with_ones = 0
                for k in range(n):
                    if grid[i][k] == 1 and grid[j][k] == 1:
                        cols_with_ones += 1
                if cols_with_ones >= 2:
                    count += cols_with_ones * (cols_with_ones - 1) // 2

        return count