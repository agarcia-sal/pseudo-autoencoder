from collections import defaultdict
from typing import List, Tuple

class Solution:
    def maximalPathQuality(self, values: List[int], edges: List[Tuple[int, int, int]], maxTime: int) -> int:
        graph = defaultdict(list)
        for u, v, time in edges:
            graph[u].append((v, time))
            graph[v].append((u, time))

        visited = set()
        max_quality = 0

        def dfs(node: int, current_time: int, current_quality: int) -> None:
            nonlocal max_quality
            if node == 0:
                if current_quality > max_quality:
                    max_quality = current_quality

            for neighbor, time in graph[node]:
                remaining_time = current_time - time
                if remaining_time >= 0:
                    if neighbor not in visited:
                        visited.add(neighbor)
                        dfs(neighbor, remaining_time, current_quality + values[neighbor])
                        visited.remove(neighbor)
                    else:
                        dfs(neighbor, remaining_time, current_quality)

        visited.add(0)
        dfs(0, maxTime, values[0])

        return max_quality