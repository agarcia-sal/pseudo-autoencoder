from typing import List, Dict, Set, Tuple
from collections import defaultdict

class Solution:
    def maximalPathQuality(self, values: List[int], edges: List[List[int]], maxTime: int) -> int:
        graph: Dict[int, List[Tuple[int, int]]] = defaultdict(list)
        for u, v, time in edges:
            graph[u].append((v, time))
            graph[v].append((u, time))

        visited: Set[int] = set()
        max_quality = 0

        def dfs(node: int, current_time: int, current_quality: int) -> None:
            nonlocal max_quality

            if node == 0:
                max_quality = max(max_quality, current_quality)

            for neighbor, t in graph[node]:
                if t <= current_time:
                    if neighbor not in visited:
                        visited.add(neighbor)
                        dfs(neighbor, current_time - t, current_quality + values[neighbor])
                        visited.remove(neighbor)
                    else:
                        dfs(neighbor, current_time - t, current_quality)

        visited.add(0)
        dfs(0, maxTime, values[0])

        return max_quality