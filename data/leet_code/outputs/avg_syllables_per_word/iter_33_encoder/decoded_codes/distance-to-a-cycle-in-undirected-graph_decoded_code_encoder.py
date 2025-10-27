from collections import defaultdict, deque
from typing import List, Optional

class Solution:
    def distanceToCycle(self, n: int, edges: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        def dfs(node: int, parent: int, path: List[int], visited: set) -> Optional[List[int]]:
            if node in visited:
                cycle_start = path.index(node)
                return path[cycle_start:]
            visited.add(node)
            path.append(node)
            for neighbor in graph[node]:
                if neighbor != parent:
                    cycle = dfs(neighbor, node, path, visited)
                    if cycle is not None:
                        return cycle
            path.pop()
            return None

        visited = set()
        cycle = None
        for node in range(n):
            if node not in visited:
                cycle = dfs(node, -1, [], visited)
                if cycle is not None:
                    break

        distance = [0] * n
        queue = deque(cycle)
        visited = set(cycle)

        level = 0
        while queue:
            for _ in range(len(queue)):
                node = queue.popleft()
                distance[node] = level
                for neighbor in graph[node]:
                    if neighbor not in visited:
                        visited.add(neighbor)
                        queue.append(neighbor)
            level += 1

        return distance