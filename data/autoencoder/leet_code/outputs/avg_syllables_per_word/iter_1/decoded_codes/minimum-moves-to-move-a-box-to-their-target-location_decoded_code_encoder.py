from collections import deque

def min_push_box(grid):
    dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    m, n = len(grid), len(grid[0])
    S = P = B = T = None
    for i in range(m):
        for j in range(n):
            if grid[i][j] == 'S':
                S = (i, j)
            elif grid[i][j] == 'B':
                B = (i, j)
            elif grid[i][j] == 'T':
                T = (i, j)

    valid = lambda pos: 0 <= pos[0] < m and 0 <= pos[1] < n and grid[pos[0]][pos[1]] != '#'

    q = deque([(S, B, 0)])
    vis = set([(S, B)])

    while q:
        p, b, c = q.popleft()
        if b == T:
            return c
        for dx, dy in dirs:
            np = (p[0] + dx, p[1] + dy)
            if valid(np):
                if np == b:
                    nb = (b[0] + dx, b[1] + dy)
                    if valid(nb) and (np, nb) not in vis:
                        vis.add((np, nb))
                        q.append((np, nb, c + 1))
                elif (np, b) not in vis:
                    vis.add((np, b))
                    q.append((np, b, c))
    return -1