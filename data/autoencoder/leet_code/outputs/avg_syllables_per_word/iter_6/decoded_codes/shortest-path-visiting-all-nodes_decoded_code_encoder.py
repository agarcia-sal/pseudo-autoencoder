from collections import deque

class Solution:
    def shortestPathLength(self, graph):
        if not graph:
            return 0

        n = len(graph)
        all_visited = (1 << n) - 1
        queue = deque((i, 1 << i) for i in range(n))
        visited = set(queue)
        steps = 0

        while queue:
            for _ in range(len(queue)):
                node, visited_nodes = queue.popleft()
                if visited_nodes == all_visited:
                    return steps
                for neighbor in graph[node]:
                    next_visited = visited_nodes | (1 << neighbor)
                    state = (neighbor, next_visited)
                    if state not in visited:
                        visited.add(state)
                        queue.append(state)
            steps += 1

        return -1