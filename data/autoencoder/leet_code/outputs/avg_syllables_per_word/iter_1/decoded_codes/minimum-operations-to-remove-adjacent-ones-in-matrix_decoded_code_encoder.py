from collections import deque

def hopcroft_karp(grid):
    rows, cols = len(grid), len(grid[0])
    n = rows * cols
    graph = [set() for _ in range(n+1)]
    match = [-1] * (n + 1)
    dist = [0] * (n + 1)

    def in_bounds(r, c):
        return 0 <= r < rows and 0 <= c < cols

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 1:
                u = r * cols + c
                for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    nr, nc = r + dr, c + dc
                    if in_bounds(nr, nc) and grid[nr][nc] == 1:
                        v = nr * cols + nc
                        graph[u].add(v)

    INF = float('inf')

    def bfs():
        Q = deque()
        for u in range(n):
            if match[u] == -1:
                dist[u] = 0
                Q.append(u)
            else:
                dist[u] = INF
        dist[-1] = INF

        while Q:
            u = Q.popleft()
            if dist[u] < dist[-1]:
                for v in graph[u]:
                    mv = match[v]
                    if dist[mv] == INF:
                        dist[mv] = dist[u] + 1
                        Q.append(mv)
        return dist[-1] != INF

    def dfs(u):
        if u == -1:
            return True
        for v in graph[u]:
            mv = match[v]
            if dist[mv] == dist[u] + 1:
                if dfs(mv):
                    match[v] = u
                    match[u] = v
                    return True
        dist[u] = INF
        return False

    matching = 0
    while bfs():
        for u in range(n):
            if match[u] == -1 and dfs(u):
                matching += 1
    return matching