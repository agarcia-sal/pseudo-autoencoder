from typing import List

class Solution:
    def maxKilledEnemies(self, grid: List[List[str]]) -> int:
        if not grid or not grid[0]:
            return 0

        m, n = len(grid), len(grid[0])
        max_kills = 0
        row_kills = 0
        col_kills = [0] * n

        for i in range(m):
            for j in range(n):
                if j == 0 or grid[i][j-1] == 'W':
                    row_kills = 0
                    for k in range(j, n):
                        if grid[i][k] == 'E':
                            row_kills += 1
                        elif grid[i][k] == 'W':
                            break

                if i == 0 or grid[i-1][j] == 'W':
                    col_kills[j] = 0
                    for k in range(i, m):
                        if grid[k][j] == 'E':
                            col_kills[j] += 1
                        elif grid[k][j] == 'W':
                            break

                if grid[i][j] == '0':
                    max_kills = max(max_kills, row_kills + col_kills[j])

        return max_kills