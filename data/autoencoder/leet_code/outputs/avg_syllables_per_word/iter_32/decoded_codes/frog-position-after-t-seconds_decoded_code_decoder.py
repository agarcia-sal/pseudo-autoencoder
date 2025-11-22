from collections import defaultdict, deque
from typing import List, Tuple

class Solution:
    def frogPosition(self, n: int, edges: List[Tuple[int, int]], t: int, target: int) -> float:
        if n == 1:
            return 1.0

        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        queue = deque([(1, 1.0, 0)])  # node, probability, time
        visited = set([1])

        while queue:
            current_node, current_prob, current_time = queue.popleft()

            # If time reached t or current node is a leaf (except node 1)
            if current_time == t or (current_node != 1 and len(graph[current_node]) == 1):
                if current_node == target:
                    return current_prob
                else:
                    continue

            # Number of unvisited neighbors (exclude parent for current_node != 1)
            possible_moves = len(graph[current_node]) - (1 if current_node != 1 else 0)
            if possible_moves == 0:
                continue

            for neighbor in graph[current_node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append((neighbor, current_prob / possible_moves, current_time + 1))

        return 0.0