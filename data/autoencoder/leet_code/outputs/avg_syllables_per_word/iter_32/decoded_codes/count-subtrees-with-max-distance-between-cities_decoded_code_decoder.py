from collections import deque
from itertools import combinations
from typing import List, Dict, Set


class Solution:
    def countSubgraphsForEachDiameter(self, n: int, edges: List[List[int]]) -> List[int]:
        # Build the undirected graph as adjacency list
        graph: Dict[int, List[int]] = {i: [] for i in range(1, n + 1)}
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        def bfs(subtree: Set[int]) -> int:
            # BFS to find the farthest node from arbitrary start node,
            # then BFS again from that farthest node to find the diameter (max distance)
            start = next(iter(subtree))
            queue = deque([start])
            visited = {start}
            farthest_node = start

            # First BFS to find one endpoint of the diameter
            while queue:
                node = queue.popleft()
                for neighbor in graph[node]:
                    if neighbor in subtree and neighbor not in visited:
                        visited.add(neighbor)
                        queue.append(neighbor)
                        farthest_node = neighbor

            # Second BFS from farthest_node to find diameter length
            queue = deque([farthest_node])
            visited = {farthest_node}
            max_distance = 0

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

        # Enumerate all subsets of size 2 to n
        nodes = range(1, n + 1)
        for size in range(2, n + 1):
            for subset in combinations(nodes, size):
                subtree = set(subset)
                # Check connectivity via DFS (implemented by stack)
                visited: Set[int] = set()
                stack = [subset[0]]
                while stack:
                    node = stack.pop()
                    if node not in visited:
                        visited.add(node)
                        for neighbor in graph[node]:
                            if neighbor in subtree and neighbor not in visited:
                                stack.append(neighbor)
                if visited == subtree:
                    diameter = bfs(subtree)
                    if diameter > 0:
                        result[diameter - 1] += 1

        return result