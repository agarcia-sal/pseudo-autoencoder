def numDistinctIslands(grid):
    rows, cols = len(grid), len(grid[0])
    unique = set()

    def dfs(i, j, d):
        if 0 <= i < rows and 0 <= j < cols and grid[i][j] == 1:
            grid[i][j] = 0
            path.append(d)
            dfs(i + 1, j, 'd')
            dfs(i - 1, j, 'u')
            dfs(i, j + 1, 'r')
            dfs(i, j - 1, 'l')
            path.append('b')
        return path

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:
                path = []
                dfs(i, j, 'o')
                unique.add(tuple(path))

    return len(unique)