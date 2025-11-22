def cherry_pickup(grid):
    rows, cols = len(grid), len(grid[0])

    from functools import lru_cache

    @lru_cache(None)
    def dp(r, c1, c2):
        if c1 < 0 or c1 >= cols or c2 < 0 or c2 >= cols:
            return 0
        result = grid[r][c1] if c1 == c2 else grid[r][c1] + grid[r][c2]
        if r != rows - 1:
            best = 0
            for dc1 in [-1, 0, 1]:
                for dc2 in [-1, 0, 1]:
                    best = max(best, dp(r + 1, c1 + dc1, c2 + dc2))
            result += best
        return result

    return dp(0, 0, cols - 1)