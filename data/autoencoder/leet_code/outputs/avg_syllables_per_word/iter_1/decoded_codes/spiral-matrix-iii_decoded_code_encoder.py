def spiralMatrixIII(rows, cols, rStart, cStart):
    dirs = [(0,1),(1,0),(0,-1),(-1,0)]
    d = 0
    steps = 0
    inc = 0
    x, y = rStart, cStart
    res = []

    while len(res) < rows * cols:
        if inc % 2 == 0:
            steps += 1
        for _ in range(steps):
            if 0 <= x < rows and 0 <= y < cols:
                res.append([x, y])
            dx, dy = dirs[d]
            x, y = x + dx, y + dy
        d = (d + 1) % 4
        inc += 1

    return res