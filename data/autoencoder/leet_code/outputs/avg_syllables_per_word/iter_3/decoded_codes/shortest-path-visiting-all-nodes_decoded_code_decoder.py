from collections import deque
from typing import List

class Solution:
    def shortestPathLength(self, graph: List[List[int]]) -> int:
        if not graph:
            return 0

        n = len(graph)
        all_visited = (1 << n) - 1
        queue = deque((i, 1 << i) for i in range(n))
        visited = set(queue)
        steps = 0

        while queue:
            for _ in range(len(queue)):
                node, state = queue.popleft()
                if state == all_visited:
                    return steps
                for neighbor in graph[node]:
                    next_state = state | (1 << neighbor)
                    next_pair = (neighbor, next_state)
                    if next_pair not in visited:
                        visited.add(next_pair)
                        queue.append(next_pair)
            steps += 1

        return -1