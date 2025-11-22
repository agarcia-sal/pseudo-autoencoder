from collections import deque
from itertools import combinations
from typing import List, Dict, Set

class Solution:
    def countSubgraphsForEachDiameter(self, n: int, edges: List[List[int]]) -> List[int]:
        graph: Dict[int, List[int]] = {i: [] for i in range(1, n + 1)}
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        def bfs(subtree: Set[int]) -> int:
            start = next(iter(subtree))
            queue = deque([start])
            visited = {start}
            farthest_node = start
            # First BFS to find the farthest node from start within subtree
            while queue:
                node = queue.popleft()
                for neighbor in graph[node]:
                    if neighbor in subtree and neighbor not in visited:
                        visited.add(neighbor)
                        queue.append(neighbor)
                        farthest_node = neighbor

            queue = deque([farthest_node])
            visited = {farthest_node}
            max_distance = 0
            # Second BFS to find the diameter (max distance) within subtree
            while queue:
                size = len(queue)
                for _ in range(size):
                    node = queue.popleft()
                    for neighbor in graph[node]:
                        if neighbor in subtree and neighbor not in visited:
                            visited.add(neighbor)
                            queue.append(neighbor)
                if queue:
                    max_distance += 1

            return max_distance

        result = [0] * (n - 1)
        nodes = range(1, n + 1)

        for size in range(2, n + 1):
            for subset in combinations(nodes, size):
                subset_set = set(subset)
                visited = set()
                stack = [subset[0]]
                while stack:
                    node = stack.pop()
                    if node not in visited:
                        visited.add(node)
                        for neighbor in graph[node]:
                            if neighbor in subset_set and neighbor not in visited:
                                stack.append(neighbor)
                if visited == subset_set:
                    diameter = bfs(subset_set)
                    if diameter > 0:
                        result[diameter - 1] += 1

        return result