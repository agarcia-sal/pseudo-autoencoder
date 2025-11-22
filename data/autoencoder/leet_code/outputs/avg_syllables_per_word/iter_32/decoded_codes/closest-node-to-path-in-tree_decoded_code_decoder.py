from collections import deque, defaultdict
from math import inf
from typing import List, Tuple

class Solution:
    def closestNode(self, n: int, edges: List[Tuple[int, int]], query: List[Tuple[int, int, int]]) -> List[int]:
        graph = defaultdict(list)
        # Build an undirected graph
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
            # If no path is found (should not happen if the graph is connected)
            return []

        def closest_node_on_path(path: List[int], node: int) -> int:
            min_distance = inf
            closest_node = None
            # For each node on the path, compute distance to 'node' and select the closest
            for p in path:
                # Distance is length(find_path(p, node)) - 1
                dist_path = find_path(p, node)
                if len(dist_path) == 0:
                    # no path found from p to node (path disconnected), skip
                    continue
                distance = len(dist_path) - 1
                if distance < min_distance:
                    min_distance = distance
                    closest_node = p
            return closest_node if closest_node is not None else -1

        answer = []
        for start, end, node in query:
            path = find_path(start, end)
            answer.append(closest_node_on_path(path, node))
        return answer