from collections import defaultdict
from typing import List, Set, Tuple

class Solution:
    def maximumCost(self, n: int, highways: List[List[int]], k: int) -> int:
        graph: defaultdict[int, List[Tuple[int, int]]] = defaultdict(list)
        for highway in highways:
            city1, city2, toll = highway
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