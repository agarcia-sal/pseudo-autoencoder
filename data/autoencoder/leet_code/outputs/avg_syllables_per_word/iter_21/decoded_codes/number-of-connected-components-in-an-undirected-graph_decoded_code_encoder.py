from typing import List, Dict, Set

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = self.create_adjacency_list(n, edges)
        visited = self.create_empty_set()

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

    def create_adjacency_list(self, n: int, edges: List[List[int]]) -> Dict[int, List[int]]:
        adjacency = {i: [] for i in range(n)}
        for a, b in edges:
            adjacency[a].append(b)
            adjacency[b].append(a)
        return adjacency

    def create_empty_set(self) -> Set[int]:
        return set()