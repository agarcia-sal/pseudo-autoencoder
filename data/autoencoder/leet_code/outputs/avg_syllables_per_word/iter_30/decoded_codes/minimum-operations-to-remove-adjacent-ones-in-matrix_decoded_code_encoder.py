from collections import deque
from math import inf

class Solution:
    def minimumOperations(self, grid):
        rows, cols = len(grid), len(grid[0])
        n = rows * cols
        graph = [set() for _ in range(n + 1)]
        match = [-1] * (n + 1)
        dist = [0] * (n + 1)

        # Build graph: edges between adjacent '1's in the grid
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    u = r * cols + c
                    for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                        nr, nc = r + dr, c + dc
                        if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                            v = nr * cols + nc
                            graph[u].add(v)

        def bfs():
            queue = deque()
            for u in range(n):
                if match[u] == -1:
                    dist[u] = 0
                    queue.append(u)
                else:
                    dist[u] = inf
            dist[-1] = inf

            while queue:
                u = queue.popleft()
                if dist[u] < dist[-1]:
                    for v in graph[u]:
                        w = match[v]
                        if dist[w] == inf:
                            dist[w] = dist[u] + 1
                            queue.append(w)
            return dist[-1] != inf

        def dfs(u):
            if u != -1:
                for v in graph[u]:
                    w = match[v]
                    if dist[w] == dist[u] + 1:
                        if dfs(w):
                            match[v] = u
                            match[u] = v
                            return True
                dist[u] = inf
                return False
            return True

        matching = 0
        while bfs():
            for u in range(n):
                if match[u] == -1 and dfs(u):
                    matching += 1

        return matching