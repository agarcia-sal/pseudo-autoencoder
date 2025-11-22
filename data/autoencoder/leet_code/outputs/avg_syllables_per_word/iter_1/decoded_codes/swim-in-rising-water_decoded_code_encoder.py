import heapq

def min_effort_path(grid):
    n = len(grid)
    visited = {(0, 0)}
    heap = [(grid[0][0], 0, 0)]
    dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    while heap:
        t, i, j = heapq.heappop(heap)
        if (i, j) == (n - 1, n - 1):
            return t
        for di, dj in dirs:
            ni, nj = i + di, j + dj
            if 0 <= ni < n and 0 <= nj < n and (ni, nj) not in visited:
                visited.add((ni, nj))
                heapq.heappush(heap, (max(t, grid[ni][nj]), ni, nj))
    return -1