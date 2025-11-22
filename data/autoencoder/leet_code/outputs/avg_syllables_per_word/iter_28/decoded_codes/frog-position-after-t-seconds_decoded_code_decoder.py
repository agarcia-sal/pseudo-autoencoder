from collections import defaultdict, deque
from typing import List

class Solution:
    def frogPosition(self, n: int, edges: List[List[int]], t: int, target: int) -> float:
        if n == 1:
            return 1.0

        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        queue = deque([(1, 1.0, 0)])  # node, probability, time
        visited = {1}

        while queue:
            node, prob, time = queue.popleft()

            if time == t or (node != 1 and len(graph[node]) == 1):
                if node == target:
                    return prob
                continue

            possible_moves = len(graph[node]) - (1 if node != 1 else 0)
            for neighbor in graph[node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append((neighbor, prob / possible_moves, time + 1))

        return 0.0