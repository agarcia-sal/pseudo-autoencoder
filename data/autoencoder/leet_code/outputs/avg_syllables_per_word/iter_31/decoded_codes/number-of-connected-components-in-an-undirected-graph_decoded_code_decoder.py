from typing import List, Dict, Set

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph: Dict[int, List[int]] = {i: [] for i in range(n)}
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)

        visited: Set[int] = set()

        def dfs(node: int) -> None:
            if node in visited:
                return
            visited.add(node)
            for neighbor in graph[node]:
                dfs(neighbor)

        components = 0
        for node in range(n):
            if node not in visited:
                dfs(node)
                components += 1

        return components