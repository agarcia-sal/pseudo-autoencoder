from collections import defaultdict, deque
from math import inf
from typing import List, Tuple, Optional

class Solution:
    def closestNode(self, n: int, edges: List[Tuple[int, int]], query: List[Tuple[int, int, int]]) -> List[Optional[int]]:
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        def find_path(start: int, end: int) -> List[int]:
            queue = deque([(start, [start])])
            visited = {start}
            while queue:
                node, path = queue.popleft()
                if node == end:
                    return path
                for neighbor in graph[node]:
                    if neighbor not in visited:
                        visited.add(neighbor)
                        queue.append((neighbor, path + [neighbor]))
            return []  # if no path found

        def closest_node_on_path(path: List[int], node: int) -> Optional[int]:
            min_distance = inf
            closest_node = None
            for p in path:
                distance = len(find_path(p, node)) - 1
                if distance < min_distance:
                    min_distance = distance
                    closest_node = p
            return closest_node

        answer = []
        for start, end, node in query:
            path = find_path(start, end)
            answer.append(closest_node_on_path(path, node))
        return answer