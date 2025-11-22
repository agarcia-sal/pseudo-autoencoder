from collections import deque
from math import inf

def maximum_minutes(grid):
    m, n = len(grid), len(grid[0])
    dirs = [(1,0), (-1,0), (0,1), (0,-1)]

    def in_bounds(x, y):
        return 0 <= x < m and 0 <= y < n

    def can_escape(wait):
        fire_t = [[inf]*n for _ in range(m)]
        q = deque()
        # Initialize fire spread time
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    q.append((i, j, 0))
                    fire_t[i][j] = 0

        # BFS for fire spreading times
        while q:
            x, y, t = q.popleft()
            for dx, dy in dirs:
                nx, ny = x + dx, y + dy
                if in_bounds(nx, ny) and grid[nx][ny] == 0 and fire_t[nx][ny] == inf:
                    fire_t[nx][ny] = t + 1
                    q.append((nx, ny, t + 1))

        # BFS for person trying to escape starting after wait time
        q = deque([(0, 0, wait)])
        visited = {(0, 0)}
        while q:
            x, y, t = q.popleft()
            for dx, dy in dirs:
                nx, ny = x + dx, y + dy
                nt = t + 1
                if in_bounds(nx, ny) and (nx, ny) not in visited and grid[nx][ny] == 0:
                    # If reached destination:
                    if (nx, ny) == (m-1, n-1):
                        # Can escape if fire arrives same time or later
                        return fire_t[nx][ny] >= nt
                    # Only move if fire arrives after person leaves cell
                    if fire_t[nx][ny] > nt:
                        visited.add((nx, ny))
                        q.append((nx, ny, nt))
        return False

    l, r = 0, m * n
    res = -1
    while l <= r:
        mid = (l + r) // 2
        if can_escape(mid):
            res = mid
            l = mid + 1
        else:
            r = mid - 1

    return 10**9 if res == m * n else res