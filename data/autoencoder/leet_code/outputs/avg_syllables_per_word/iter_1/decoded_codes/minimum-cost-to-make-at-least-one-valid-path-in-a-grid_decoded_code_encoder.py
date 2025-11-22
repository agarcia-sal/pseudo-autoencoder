import heapq
import math

def min_cost(grid):
    m, n = len(grid), len(grid[0])
    dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    costs = [[math.inf] * n for _ in range(m)]
    costs[0][0] = 0
    pq = [(0, 0, 0)]  # (cost, i, j)
    visited = set()

    def in_bounds(x, y):
        return 0 <= x < m and 0 <= y < n

    while pq:
        c, i, j = heapq.heappop(pq)
        if (i, j) in visited:
            continue
        visited.add((i, j))
        if i == m - 1 and j == n - 1:
            return c
        for k, (di, dj) in enumerate(dirs):
            ni, nj = i + di, j + dj
            if in_bounds(ni, nj):
                nc = c + (1 if (k + 1) != grid[i][j] else 0)
                if nc < costs[ni][nj]:
                    costs[ni][nj] = nc
                    heapq.heappush(pq, (nc, ni, nj))
    return -1