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
                node, mask = queue.popleft()
                if mask == all_visited:
                    return steps
                for nei in graph[node]:
                    next_mask = mask | (1 << nei)
                    state = (nei, next_mask)
                    if state not in visited:
                        visited.add(state)
                        queue.append(state)
            steps += 1

        return -1