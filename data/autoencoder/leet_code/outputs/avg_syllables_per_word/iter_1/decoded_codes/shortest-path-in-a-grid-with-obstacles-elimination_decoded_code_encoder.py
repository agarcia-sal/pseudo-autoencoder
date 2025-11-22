from collections import deque

def shortest_path_with_obstacles(grid, k):
    if not grid or not grid[0]:
        return -1
    m, n = len(grid), len(grid[0])
    if k >= m + n - 2:
        return m + n - 2

    def in_bounds(x, y):
        return 0 <= x < m and 0 <= y < n

    dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    Q = deque([(0, 0, k, 0)])
    vis = {(0, 0, k)}

    while Q:
        x, y, r, steps = Q.popleft()
        if x == m - 1 and y == n - 1:
            return steps
        for dx, dy in dirs:
            nx, ny = x + dx, y + dy
            if in_bounds(nx, ny):
                nr = r - grid[nx][ny]
                if nr >= 0 and (nx, ny, nr) not in vis:
                    vis.add((nx, ny, nr))
                    Q.append((nx, ny, nr, steps + 1))
    return -1