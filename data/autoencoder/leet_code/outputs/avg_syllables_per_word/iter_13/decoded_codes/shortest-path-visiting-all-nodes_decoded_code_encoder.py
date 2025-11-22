from collections import deque

class Solution:
    def shortestPathLength(self, graph):
        if not graph:
            return 0

        n = len(graph)
        queue = deque((i, 1 << i) for i in range(n))
        visited = set(queue)
        all_nodes_visited = (1 << n) - 1
        steps = 0

        while queue:
            for _ in range(len(queue)):
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