from collections import deque

class Solution:
    def minimumOperations(self, grid):
        def bfs():
            queue = deque()
            for u in range(n):
                if match[u] == -1:
                    dist[u] = 0
                    queue.append(u)
                else:
                    dist[u] = float('inf')
            dist[-1] = float('inf')

            while queue:
                u = queue.popleft()
                if dist[u] < dist[-1]:
                    for v in graph[u]:
                        mv = match[v]
                        if dist[mv] == float('inf'):
                            dist[mv] = dist[u] + 1
                            queue.append(mv)
            return dist[-1] < float('inf')

        def dfs(u):
            if u != -1:
                for v in graph[u]:
                    mv = match[v]
                    if dist[mv] == dist[u] + 1:
                        if dfs(mv):
                            match[v] = u
                            match[u] = v
                            return True
                dist[u] = float('inf')
                return False
            return True

        rows = len(grid)
        cols = len(grid[0]) if rows else 0
        n = rows * cols

        graph = [set() for _ in range(n + 1)]
        match = [-1] * (n + 1)
        dist = [0] * (n + 1)

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    u = r * cols + c
                    for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                        nr, nc = r + dr, c + dc
                        if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                            v = nr * cols + nc
                            graph[u].add(v)

        matching = 0
        while bfs():
            for u in range(n):
                if match[u] == -1 and dfs(u):
                    matching += 1
        return matching