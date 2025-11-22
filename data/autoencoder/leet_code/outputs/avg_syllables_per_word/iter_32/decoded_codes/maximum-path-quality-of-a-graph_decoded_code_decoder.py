from collections import defaultdict
from typing import List


class Solution:
    def maximalPathQuality(self, values: List[int], edges: List[List[int]], maxTime: int) -> int:
        # Build graph as adjacency list: node -> list of (neighbor, time)
        graph = defaultdict(list)
        for edge in edges:
            u, v, time = edge
            graph[u].append((v, time))
            graph[v].append((u, time))

        max_quality = 0
        visited = set()

        def dfs(node: int, current_time: int, current_quality: int) -> None:
            nonlocal max_quality

            if node == 0:
                if current_quality > max_quality:
                    max_quality = current_quality

            for neighbor, time in graph[node]:
                if time <= current_time:
                    if neighbor not in visited:
                        visited.add(neighbor)
                        dfs(neighbor, current_time - time, current_quality + values[neighbor])
                        visited.remove(neighbor)
                    else:
                        dfs(neighbor, current_time - time, current_quality)

        visited.add(0)
        dfs(0, maxTime, values[0])

        return max_quality