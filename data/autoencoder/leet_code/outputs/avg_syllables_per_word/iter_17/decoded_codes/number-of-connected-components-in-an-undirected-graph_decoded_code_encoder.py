from collections import defaultdict
from typing import List, Dict, Set

def createGraph(n: int, edges: List[List[int]]) -> Dict[int, List[int]]:
    graph = {i: [] for i in range(n)}
    for a, b in edges:
        graph[a].append(b)
        graph[b].append(a)
    return graph

def createVisitedSet() -> Set[int]:
    return set()

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = createGraph(n, edges)
        visited = createVisitedSet()

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