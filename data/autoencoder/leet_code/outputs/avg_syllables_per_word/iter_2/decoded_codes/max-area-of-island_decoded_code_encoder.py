from typing import List

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0

        max_area = 0
        rows = len(grid)
        cols = len(grid[0])

        def dfs(r: int, c: int) -> int:
            if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] == 0:
                return 0

            grid[r][c] = 0
            area = 1

            area += dfs(r + 1, c)
            area += dfs(r - 1, c)
            area += dfs(r, c + 1)
            area += dfs(r, c - 1)

            return area

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    current_area = dfs(r, c)
                    if current_area > max_area:
                        max_area = current_area

        return max_area