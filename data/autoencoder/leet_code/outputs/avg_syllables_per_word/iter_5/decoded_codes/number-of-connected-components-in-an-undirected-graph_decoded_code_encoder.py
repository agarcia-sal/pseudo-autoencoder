class Solution:
    def countComponents(self, n, edges):
        graph = {i: [] for i in range(n)}
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)
        visited = set()

        def dfs(node):
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