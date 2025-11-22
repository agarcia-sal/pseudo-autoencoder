def max_killed_enemies(grid):
    if not grid or not grid[0]:
        return 0

    m, n = len(grid), len(grid[0])
    max_k = 0
    col_kills = [0] * n

    def count_right_enemies(i, j):
        count = 0
        while j < n and grid[i][j] != 'W':
            if grid[i][j] == 'E':
                count += 1
            j += 1
        return count

    def count_down_enemies(i, j):
        count = 0
        while i < m and grid[i][j] != 'W':
            if grid[i][j] == 'E':
                count += 1
            i += 1
        return count

    for i in range(m):
        row_k = 0
        for j in range(n):
            if j == 0 or grid[i][j - 1] == 'W':
                row_k = count_right_enemies(i, j)
            if i == 0 or grid[i - 1][j] == 'W':
                col_kills[j] = count_down_enemies(i, j)
            if grid[i][j] == '0':
                max_k = max(max_k, row_k + col_kills[j])

    return max_k