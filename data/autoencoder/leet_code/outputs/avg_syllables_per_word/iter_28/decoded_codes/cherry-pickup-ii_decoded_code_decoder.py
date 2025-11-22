from typing import List
from functools import lru_cache

class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0]) if grid else 0

        @lru_cache(None)
        def dp(r: int, c1: int, c2: int) -> int:
            if c1 < 0 or c1 >= cols or c2 < 0 or c2 >= cols:
                return 0

            cherries = grid[r][c1] if c1 == c2 else grid[r][c1] + grid[r][c2]

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