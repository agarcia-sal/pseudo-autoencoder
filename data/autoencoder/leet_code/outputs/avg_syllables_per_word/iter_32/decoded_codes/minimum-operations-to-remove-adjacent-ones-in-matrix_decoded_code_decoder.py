from collections import deque
from math import inf
from typing import List

class Solution:
    def minimumOperations(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0]) if grid else 0
        n = rows * cols

        graph = [set() for _ in range(n + 1)]
        match = [-1] * (n + 1)
        dist = [0] * (n + 1)

        # Build the graph (edges between adjacent cells with value 1)
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    u = r * cols + c
                    for dr, dc in directions:
                        nr, nc = r + dr, c + dc
                        if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                            v = nr * cols + nc
                            graph[u].add(v)

        def bfs() -> bool:
            queue = deque()
            for u in range(n):
                if match[u] == -1:
                    dist[u] = 0
                    queue.append(u)
                else:
                    dist[u] = inf
            dist[-1] = inf  # Dist for the "nil" node

            while queue:
                u = queue.popleft()
                if dist[u] < dist[-1]:
                    for v in graph[u]:
                        mv = match[v]
                        if mv == -1:
                            # if match[v] is -1, dist[-1] is inf which is not necessarily infinity condition.
                            # Just treat it normally:
                            if dist[-1] == inf:
                                dist[-1] = dist[u] + 1
                        if mv != -1 and dist[mv] == inf:
                            dist[mv] = dist[u] + 1
                            queue.append(mv)
            return dist[-1] < inf

        def dfs(u: int) -> bool:
            if u == -1:
                return True
            for v in graph[u]:
                mv = match[v]
                if mv == -1:
                    # Can't check dist[mv] == dist[u] + 1 if mv == -1. This vertex is unmatched right now.
                    # To respect the pseudocode, only follow edges if dist[match[v]] == dist[u] + 1.
                    # But if match[v] == -1, dist[-1] is used.
                    if dist[-1] == dist[u] + 1:
                        if dfs(-1):
                            match[v] = u
                            match[u] = v
                            return True
                elif dist[mv] == dist[u] + 1:
                    if dfs(mv):
                        match[v] = u
                        match[u] = v
                        return True
            dist[u] = inf
            return False

        # Correct bfs and dfs implementation referencing pseudocode:
        # The pseudocode uses dist[-1] as a special value:
        #   In Python, dist[-1] means last element, which is dist[n]
        #   dist size is n+1, dist[n] reserved as "null" or "nil" vertex distance.
        # match also sized n+1, with match[n] = -1 usually
        # For neighbors v in graph[u], we consider dist[match[v]]
        # So needs to be exact on indexing.

        # Rewrite bfs and dfs fully following pseudocode:
        def bfs() -> bool:
            queue = deque()
            for u in range(n):
                if match[u] == -1:
                    dist[u] = 0
                    queue.append(u)
                else:
                    dist[u] = inf
            dist[n] = inf  # special "nil" vertex

            while queue:
                u = queue.popleft()
                if dist[u] < dist[n]:
                    for v in graph[u]:
                        mv = match[v]
                        if mv == -1:
                            if dist[n] == inf:
                                dist[n] = dist[u] + 1
                        elif dist[mv] == inf:
                            dist[mv] = dist[u] + 1
                            queue.append(mv)
            return dist[n] != inf

        def dfs(u: int) -> bool:
            if u == -1:
                return True
            for v in graph[u]:
                mv = match[v]
                if mv == -1:
                    # Only if dist[n] == dist[u] + 1 proceed to dfs(-1)
                    if dist[n] == dist[u] + 1:
                        if dfs(-1):
                            match[v] = u
                            match[u] = v
                            return True
                elif dist[mv] == dist[u] + 1:
                    if dfs(mv):
                        match[v] = u
                        match[u] = v
                        return True
            dist[u] = inf
            return False

        matching = 0
        while bfs():
            for u in range(n):
                if match[u] == -1 and dfs(u):
                    matching += 1

        return matching