from collections import deque
from typing import List

class Solution:
    def shortestPathLength(self, graph: List[List[int]]) -> int:
        if not graph:
            return 0

        n = len(graph)
        queue = deque((node, 1 << node) for node in range(n))
        visited = set((node, 1 << node) for node in range(n))

        steps = 0
        all_nodes_visited = (1 << n) - 1

        while queue:
            current_level_size = len(queue)
            for _ in range(current_level_size):
                current_node, visited_nodes = queue.popleft()

                if visited_nodes == all_nodes_visited:
                    return steps

                for neighbor in graph[current_node]:
                    next_visited_nodes = visited_nodes | (1 << neighbor)
                    next_state = (neighbor, next_visited_nodes)

                    if next_state not in visited:
                        visited.add(next_state)
                        queue.append(next_state)

            steps += 1

        return -1