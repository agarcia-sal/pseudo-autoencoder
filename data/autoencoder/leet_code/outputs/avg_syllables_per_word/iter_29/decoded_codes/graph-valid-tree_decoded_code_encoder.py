from collections import defaultdict

class Solution:
    def validTree(self, n: int, edges: list[list[int]]) -> bool:
        if len(edges) != n - 1:
            return False

        adjacency_list = defaultdict(list)
        for a, b in edges:
            adjacency_list[a].append(b)
            adjacency_list[b].append(a)

        visited_nodes = set()

        def dfs(node: int) -> None:
            if node in visited_nodes:
                return
            visited_nodes.add(node)
            for neighbor in adjacency_list[node]:
                dfs(neighbor)

        dfs(0)

        return len(visited_nodes) == n