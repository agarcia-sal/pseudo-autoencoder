from collections import deque

class Solution:
    def minimumOperations(self, grid):
        rows = len(grid)
        cols = len(grid[0]) if rows > 0 else 0
        n = rows * cols

        graph = [set() for _ in range(n + 1)]
        match = [-1] * (n + 1)
        dist = [0] * (n + 1)

        # Build graph connecting adjacent 1's
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    u = r * cols + c
                    for dr, dc in [(-1,0), (1,0), (0,-1), (0,1)]:
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
                    dist[u] = float('inf')
            dist[-1] = float('inf')
            while queue:
                u = queue.popleft()
                if dist[u] < dist[-1]:
                    for v in graph[u]:
                        w = match[v]
                        if w != -1 and dist[w] == float('inf'):
                            dist[w] = dist[u] + 1
                            queue.append(w)
                        elif w == -1 and dist[-1] == float('inf'):
                            dist[-1] = dist[u] + 1
            return dist[-1] != float('inf')

        def dfs(u):
            if u != -1:
                for v in graph[u]:
                    w = match[v]
                    if w == -1 or (dist[w] == dist[u] + 1 and dfs(w)):
                        match[v] = u
                        match[u] = v
                        return True
                dist[u] = float('inf')
                return False
            return True

        matching = 0
        while bfs():
            for u in range(n):
                if match[u] == -1 and dfs(u):
                    matching += 1

        return matching