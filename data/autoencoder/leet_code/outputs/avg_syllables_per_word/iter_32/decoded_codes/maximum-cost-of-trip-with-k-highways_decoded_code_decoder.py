from collections import defaultdict
from typing import List, Tuple, Set

class Solution:
    def maximumCost(self, n: int, highways: List[Tuple[int, int, int]], k: int) -> int:
        graph = defaultdict(list)  # city -> list of (neighbor, toll)
        for city1, city2, toll in highways:
            graph[city1].append((city2, toll))
            graph[city2].append((city1, toll))

        max_cost = -1

        def dfs(city: int, visited: Set[int], cost: int, highways_used: int) -> None:
            nonlocal max_cost
            if highways_used == k:
                if cost > max_cost:
                    max_cost = cost
                return
            for neighbor, toll in graph[city]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    dfs(neighbor, visited, cost + toll, highways_used + 1)
                    visited.remove(neighbor)

        for start_city in range(n):
            visited = {start_city}
            dfs(start_city, visited, 0, 0)

        return max_cost