from collections import deque
import math

def shortestDistance(grid):
    if not grid or not grid[0]:
        return -1

    m, n = len(grid), len(grid[0])
    total_dist = [[0]*n for _ in range(m)]
    reach = [[0]*n for _ in range(m)]
    buildings = 0
    dirs = [(1,0), (-1,0), (0,1), (0,-1)]

    def bfs(sx, sy):
        q = deque([(sx, sy)])
        visited = [[False]*n for _ in range(m)]
        visited[sx][sy] = True
        dist = 0
        reachable = 0

        while q:
            dist += 1
            for _ in range(len(q)):
                x, y = q.popleft()
                for dx, dy in dirs:
                    nx, ny = x+dx, y+dy
                    if 0 <= nx < m and 0 <= ny < n and not visited[nx][ny] and grid[nx][ny] == 0:
                        visited[nx][ny] = True
                        q.append((nx, ny))
                        total_dist[nx][ny] += dist
                        reach[nx][ny] += 1
                        reachable += 1
        return reachable

    for i in range(m):
        for j in range(n):
            if grid[i][j] == 1:
                buildings += 1
                if bfs(i, j) < buildings - 1:
                    return -1

    min_dist = math.inf
    for i in range(m):
        for j in range(n):
            if grid[i][j] == 0 and reach[i][j] == buildings:
                min_dist = min(min_dist, total_dist[i][j])

    return min_dist if min_dist != math.inf else -1