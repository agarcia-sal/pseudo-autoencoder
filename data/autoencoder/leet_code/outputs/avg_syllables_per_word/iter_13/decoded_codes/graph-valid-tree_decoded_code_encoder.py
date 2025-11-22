class Solution:
    def validTree(self, n: int, edges: list[list[int]]) -> bool:
        if len(edges) != n - 1:
            return False
        adj_list = {i: [] for i in range(n)}
        for node_a, node_b in edges:
            adj_list[node_a].append(node_b)
            adj_list[node_b].append(node_a)
        visited = set()
        def dfs(node: int) -> None:
            if node in visited:
                return
            visited.add(node)
            for neighbor in adj_list[node]:
                dfs(neighbor)
        dfs(0)
        return len(visited) == n