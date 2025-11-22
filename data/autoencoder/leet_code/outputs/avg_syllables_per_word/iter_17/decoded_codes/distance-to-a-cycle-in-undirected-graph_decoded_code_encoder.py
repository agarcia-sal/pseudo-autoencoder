from collections import defaultdict, deque

class Solution:
    def distanceToCycle(self, n: int, edges: list[list[int]]) -> list[int]:
        graph = defaultdict(list)
        for node_u, node_v in edges:
            graph[node_u].append(node_v)
            graph[node_v].append(node_u)

        def dfs(node: int, parent: int, path: list[int], visited: set[int]) -> list[int] | None:
            if node in visited:
                cycle_start_position = path.index(node)
                return path[cycle_start_position:]
            visited.add(node)
            path.append(node)
            for neighbor in graph[node]:
                if neighbor != parent:
                    cycle_result = dfs(neighbor, node, path, visited)
                    if cycle_result is not None:
                        return cycle_result
            path.pop()
            return None

        visited: set[int] = set()
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
            current_queue_length = len(queue)
            for _ in range(current_queue_length):
                current_node = queue.popleft()
                distance[current_node] = level
                for neighbor in graph[current_node]:
                    if neighbor not in visited:
                        visited.add(neighbor)
                        queue.append(neighbor)
            level += 1

        return distance