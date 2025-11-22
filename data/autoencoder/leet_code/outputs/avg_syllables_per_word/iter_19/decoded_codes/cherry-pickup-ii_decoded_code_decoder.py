from functools import lru_cache

class Solution:
    def cherryPickup(self, grid):
        rows = len(grid)
        cols = len(grid[0])

        @lru_cache(None)
        def dp(r, c1, c2):
            # Check column boundaries
            if c1 < 0 or c1 >= cols or c2 < 0 or c2 >= cols:
                return 0
            # Collect cherries at current positions; avoid double count if same cell
            cherries = grid[r][c1] if c1 == c2 else grid[r][c1] + grid[r][c2]
            # If at last row, return cherries collected here
            if r == rows - 1:
                return cherries
            max_cherries = 0
            # Explore all moves for both robots
            for dc1 in (-1, 0, 1):
                for dc2 in (-1, 0, 1):
                    candidate = dp(r + 1, c1 + dc1, c2 + dc2)
                    if candidate > max_cherries:
                        max_cherries = candidate
            return cherries + max_cherries

        return dp(0, 0, cols - 1)