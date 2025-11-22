def diagonal_traverse(mat):
    if not mat or not mat[0]:
        return []
    m, n = len(mat), len(mat[0])
    r, c, dir = 0, 0, 1
    res = []

    for _ in range(m * n):
        res.append(mat[r][c])
        nr = r + (-1 if dir == 1 else 1)
        nc = c + (1 if dir == 1 else -1)

        if nr < 0 or nr == m or nc < 0 or nc == n:
            if dir == 1:
                if nc == n:
                    nr, nc = r + 1, c
                else:
                    nr, nc = 0, c + 1
            else:
                if nr == m:
                    nr, nc = r, c + 1
                else:
                    nr, nc = r + 1, 0
            dir = -dir
        r, c = nr, nc

    return res