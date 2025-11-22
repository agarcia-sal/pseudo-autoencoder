from typing import List

class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n = len(graph)
        visited = [0] * n  # 0 = unvisited, 1 = visiting, 2 = safe

        def is_safe(node: int) -> bool:
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

        safe_nodes = []
        for node in range(n):
            if is_safe(node):
                safe_nodes.append(node)

        return safe_nodes