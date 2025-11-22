from collections import defaultdict
from typing import List, Tuple

class Solution:
    def maximalPathQuality(self, values: List[int], edges: List[List[int]], maxTime: int) -> int:
        graph = defaultdict(list)
        for u, v, time in edges:
            graph[u].append((v, time))
            graph[v].append((u, time))

        visited = set()
        max_quality = 0

        def dfs(node: int, time_left: int, current_quality: int) -> None:
            nonlocal max_quality
            if node == 0:
                if current_quality > max_quality:
                    max_quality = current_quality

            for neighbor, time_needed in graph[node]:
                if time_needed <= time_left:
                    if neighbor not in visited:
                        visited.add(neighbor)
                        dfs(neighbor, time_left - time_needed, current_quality + values[neighbor])
                        visited.remove(neighbor)
                    else:
                        dfs(neighbor, time_left - time_needed, current_quality)

        visited.add(0)
        dfs(0, maxTime, values[0])

        return max_quality