from collections import defaultdict
from typing import List, Set, Tuple

class Solution:
    def maximalPathQuality(self, values: List[int], edges: List[List[int]], maxTime: int) -> int:
        graph = defaultdict(list)  # node -> list of (neighbor, time)
        for u, v, time in edges:
            graph[u].append((v, time))
            graph[v].append((u, time))

        max_quality = 0
        visited: Set[int] = set()

        def dfs(node: int, remaining_time: int, current_quality: int) -> None:
            nonlocal max_quality
            if node == 0:
                max_quality = max(max_quality, current_quality)

            for neighbor, time_cost in graph[node]:
                if time_cost <= remaining_time:
                    if neighbor not in visited:
                        visited.add(neighbor)
                        dfs(neighbor, remaining_time - time_cost, current_quality + values[neighbor])
                        visited.remove(neighbor)
                    else:
                        # Visiting already visited node, quality doesn't increase
                        dfs(neighbor, remaining_time - time_cost, current_quality)

        visited.add(0)
        dfs(0, maxTime, values[0])
        return max_quality