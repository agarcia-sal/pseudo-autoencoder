class Solution:
    def eventualSafeNodes(self, graph):
        def is_safe(node):
            if visited[node] == 1:
                return False
            if visited[node] == 2:
                return True
            visited[node] = 1
            for neighbor in graph[node]:
                if not is_safe(neighbor):
                    return False
            visited[node] = 2
            return True

        n = len(graph)
        visited = [0] * n
        safe_nodes = []
        for node in range(n):
            if is_safe(node):
                safe_nodes.append(node)
        return safe_nodes