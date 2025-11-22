class Solution:
    def uniquePathsIII(self, grid):
        m, n = len(grid), len(grid[0])
        start_x = start_y = 0
        empty_squares = 1

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    start_x, start_y = i, j
                elif grid[i][j] == 0:
                    empty_squares += 1

        def dfs(x, y, steps):
            if grid[x][y] == 2:
                return steps == 0

            original = grid[x][y]
            grid[x][y] = -1
            count = 0

            for dx, dy in ((1,0), (-1,0), (0,1), (0,-1)):
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] >= 0:
                    count += dfs(nx, ny, steps - 1)

            grid[x][y] = original
            return count

        return dfs(start_x, start_y, empty_squares)