class Solution:
    def maxKilledEnemies(self, grid):
        if not grid or not grid[0]:
            return 0

        rows, cols = len(grid), len(grid[0])
        max_kills = 0
        row_kills = 0
        col_kills = [0] * cols

        for r in range(rows):
            for c in range(cols):
                if c == 0 or grid[r][c - 1] == 'W':
                    row_kills = 0
                    for k in range(c, cols):
                        if grid[r][k] == 'W':
                            break
                        elif grid[r][k] == 'E':
                            row_kills += 1

                if r == 0 or grid[r - 1][c] == 'W':
                    col_kills[c] = 0
                    for k in range(r, rows):
                        if grid[k][c] == 'W':
                            break
                        elif grid[k][c] == 'E':
                            col_kills[c] += 1

                if grid[r][c] == '0':
                    max_kills = max(max_kills, row_kills + col_kills[c])

        return max_kills