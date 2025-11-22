from collections import defaultdict
from typing import List

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1:
            return False

        adj_list = defaultdict(list)
        for a, b in edges:
            adj_list[a].append(b)
            adj_list[b].append(a)

        visited = set()

        def dfs(node: int) -> None:
            if node in visited:
                return
            visited.add(node)
            for neighbor in adj_list[node]:
                dfs(neighbor)

        dfs(0)
        return len(visited) == n