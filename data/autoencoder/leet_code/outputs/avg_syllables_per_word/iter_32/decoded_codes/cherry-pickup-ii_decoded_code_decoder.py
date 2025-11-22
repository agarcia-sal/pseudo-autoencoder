from functools import lru_cache
from typing import List

class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0]) if rows > 0 else 0

        @lru_cache(None)
        def dp(r: int, c1: int, c2: int) -> int:
            # Boundary checks for columns
            if c1 < 0 or c1 >= cols or c2 < 0 or c2 >= cols:
                return 0

            # Collect cherries at the current row: if c1 == c2, count once; else sum both
            cherries = grid[r][c1] if c1 == c2 else grid[r][c1] + grid[r][c2]

            # If at last row, return collected cherries
            if r == rows - 1:
                return cherries

            max_cherries = 0
            for dc1 in (-1, 0, 1):
                for dc2 in (-1, 0, 1):
                    candidate = dp(r + 1, c1 + dc1, c2 + dc2)
                    if candidate > max_cherries:
                        max_cherries = candidate

            return cherries + max_cherries

        return dp(0, 0, cols - 1)