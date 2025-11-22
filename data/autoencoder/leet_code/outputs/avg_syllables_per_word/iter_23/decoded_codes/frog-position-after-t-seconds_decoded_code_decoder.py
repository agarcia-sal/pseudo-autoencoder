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

        queue = deque([(1, 1.0, 0)])
        visited = {1}

        while queue:
            current_node, current_probability, current_time = queue.popleft()

            # Check if time is reached or if current node is a leaf (except node 1)
            if current_time == t or (current_node != 1 and len(graph[current_node]) == 1):
                if current_node == target:
                    return current_probability
                else:
                    continue

            # Number of possible moves (exclude parent node, except for node 1)
            possible_moves = len(graph[current_node]) - 1 if current_node != 1 else len(graph[current_node])
            if possible_moves == 0:
                # No moves possible, frog stays
                if current_node == target:
                    return current_probability
                else:
                    continue

            for neighbor in graph[current_node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append((neighbor, current_probability / possible_moves, current_time + 1))

        return 0.0