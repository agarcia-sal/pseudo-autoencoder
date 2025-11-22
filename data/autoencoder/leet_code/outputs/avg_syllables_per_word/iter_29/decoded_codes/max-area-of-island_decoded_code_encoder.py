from typing import List

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0

        rows, cols = len(grid), len(grid[0])

        def dfs(row: int, column: int) -> int:
            if row < 0 or row >= rows or column < 0 or column >= cols or grid[row][column] == 0:
                return 0
            grid[row][column] = 0
            area = 1
            area += dfs(row + 1, column)
            area += dfs(row - 1, column)
            area += dfs(row, column + 1)
            area += dfs(row, column - 1)
            return area

        max_area = 0
        for row in range(rows):
            for column in range(cols):
                if grid[row][column] == 1:
                    max_area = max(max_area, dfs(row, column))

        return max_area