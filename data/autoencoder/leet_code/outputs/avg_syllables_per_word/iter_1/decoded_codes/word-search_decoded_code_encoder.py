def exist(board, word):
    if not board or not board[0]:
        return False
    m, n = len(board), len(board[0])
    visited = [[False] * n for _ in range(m)]

    def dfs(x, y, i):
        if i == len(word):
            return True
        if x < 0 or x >= m or y < 0 or y >= n or visited[x][y] or board[x][y] != word[i]:
            return False
        visited[x][y] = True
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            if dfs(x + dx, y + dy, i + 1):
                return True
        visited[x][y] = False
        return False

    for i in range(m):
        for j in range(n):
            if dfs(i, j, 0):
                return True
    return False