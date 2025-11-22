def uniquePathsIII(grid):
    m, n = len(grid), len(grid[0])
    start_x, start_y, empty = 0, 0, 1
    for i in range(m):
        for j in range(n):
            if grid[i][j] == 1:
                start_x, start_y = i, j
            elif grid[i][j] == 0:
                empty += 1

    def dfs(x, y, steps):
        if grid[x][y] == 2:
            return steps == 0
        save = grid[x][y]
        grid[x][y] = -2
        total = 0
        for dx, dy in [(-1,0), (1,0), (0,-1), (0,1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] >= 0:
                total += dfs(nx, ny, steps - 1)
        grid[x][y] = save
        return total

    return dfs(start_x, start_y, empty)