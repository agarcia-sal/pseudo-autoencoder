from collections import defaultdict, deque

class Solution:
    def frogPosition(self, n: int, edges: list[list[int]], t: int, target: int) -> float:
        if n == 1:
            return 1.0

        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        queue = deque([(1, 1.0, 0)])  # (current_node, current_probability, current_time)
        visited = {1}

        while queue:
            current_node, current_probability, current_time = queue.popleft()

            if current_time == t or (current_node != 1 and len(graph[current_node]) == 1):
                if current_node == target:
                    return current_probability
                continue

            possible_moves = len(graph[current_node]) - 1 if current_node != 1 else len(graph[current_node])

            for neighbor in graph[current_node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append((neighbor, current_probability / possible_moves, current_time + 1))

        return 0.0