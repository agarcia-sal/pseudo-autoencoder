from functools import lru_cache

class Solution:
    def cherryPickup(self, grid):
        rows = len(grid)
        cols = len(grid[0]) if rows > 0 else 0

        @lru_cache(None)
        def dp(r, c1, c2):
            if c1 < 0 or c1 >= cols or c2 < 0 or c2 >= cols:
                return 0

            if c1 == c2:
                cherries = grid[r][c1]
            else:
                cherries = grid[r][c1] + grid[r][c2]

            if r == rows - 1:
                return cherries

            max_cherries = 0
            for dc1 in (-1, 0, 1):
                for dc2 in (-1, 0, 1):
                    new_value = dp(r + 1, c1 + dc1, c2 + dc2)
                    if new_value > max_cherries:
                        max_cherries = new_value

            return cherries + max_cherries

        return dp(0, 0, cols - 1)