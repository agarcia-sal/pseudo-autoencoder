from typing import List, Optional

class Solution:
    def maxKilledEnemies(self, grid: Optional[List[List[str]]]) -> int:
        if not grid or not grid[0]:
            return 0

        m, n = len(grid), len(grid[0])
        max_kills = 0

        row_kills = 0
        col_kills = [0] * n

        for i in range(m):
            for j in range(n):
                if j == 0 or grid[i][j-1] == 'wall':
                    row_kills = 0
                    for k in range(j, n):
                        if grid[i][k] == 'enemy':
                            row_kills += 1
                        elif grid[i][k] == 'wall':
                            break

                if i == 0 or grid[i-1][j] == 'wall':
                    col_kills[j] = 0
                    for k in range(i, m):
                        if grid[k][j] == 'enemy':
                            col_kills[j] += 1
                        elif grid[k][j] == 'wall':
                            break

                if grid[i][j] == '0':
                    max_kills = max(max_kills, row_kills + col_kills[j])

        return max_kills