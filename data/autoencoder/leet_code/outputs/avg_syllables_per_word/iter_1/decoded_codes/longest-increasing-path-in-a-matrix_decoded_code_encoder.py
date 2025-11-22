def longest_increasing_path(matrix):
    if not matrix or not matrix[0]:
        return 0

    m, n = len(matrix), len(matrix[0])
    dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    dp = [[-1] * n for _ in range(m)]

    def dfs(x, y):
        if dp[x][y] != -1:
            return dp[x][y]
        max_len = 1
        for dx, dy in dirs:
            nx, ny = x + dx, y + dy
            if 0 <= nx < m and 0 <= ny < n and matrix[nx][ny] > matrix[x][y]:
                max_len = max(max_len, 1 + dfs(nx, ny))
        dp[x][y] = max_len
        return max_len

    res = 0
    for i in range(m):
        for j in range(n):
            res = max(res, dfs(i, j))

    return res