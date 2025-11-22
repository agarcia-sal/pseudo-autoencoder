from functools import cache
from typing import List

class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        @cache
        def dp(r: int, c1: int, c2: int) -> int:
            if c1 < 0 or c1 >= cols or c2 < 0 or c2 >= cols:
                return 0

            cherries = grid[r][c1] if c1 == c2 else grid[r][c1] + grid[r][c2]

            if r == rows - 1:
                return cherries

            max_cherries = 0
            for dc1 in (-1, 0, 1):
                for dc2 in (-1, 0, 1):
                    temp = dp(r + 1, c1 + dc1, c2 + dc2)
                    if temp > max_cherries:
                        max_cherries = temp

            return cherries + max_cherries

        return dp(0, 0, cols - 1)