def longestLine(mat):
    if not mat or not mat[0]:
        return 0
    m, n = len(mat), len(mat[0])
    directions = [(0, 1), (1, 0), (1, 1), (1, -1)]
    max_len = 0

    def check(x, y, dx, dy):
        length = 0
        while 0 <= x < m and 0 <= y < n and mat[x][y] == 1:
            length += 1
            x += dx
            y += dy
        return length

    for i in range(m):
        for j in range(n):
            if mat[i][j] == 1:
                for dx, dy in directions:
                    if i - dx < 0 or j - dy < 0 or j - dy >= n or mat[i - dx][j - dy] == 0:
                        max_len = max(max_len, check(i, j, dx, dy))

    return max_len