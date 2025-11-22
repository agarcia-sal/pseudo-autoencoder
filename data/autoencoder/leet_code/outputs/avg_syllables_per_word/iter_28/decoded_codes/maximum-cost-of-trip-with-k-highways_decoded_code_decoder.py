from collections import defaultdict
from typing import List, Tuple

class Solution:
    def maximumCost(self, n: int, highways: List[Tuple[int, int, int]], k: int) -> int:
        graph = defaultdict(list)
        for city_one, city_two, toll_value in highways:
            graph[city_one].append((city_two, toll_value))
            graph[city_two].append((city_one, toll_value))

        max_cost_value = -1

        def dfs(current_city: int, visited_cities: set, current_cost: int, highways_count: int) -> None:
            nonlocal max_cost_value
            if highways_count == k:
                if current_cost > max_cost_value:
                    max_cost_value = current_cost
                return
            for neighbor_city, neighbor_toll in graph[current_city]:
                if neighbor_city not in visited_cities:
                    visited_cities.add(neighbor_city)
                    dfs(neighbor_city, visited_cities, current_cost + neighbor_toll, highways_count + 1)
                    visited_cities.remove(neighbor_city)

        for start_city in range(n):
            visited_set = {start_city}
            dfs(start_city, visited_set, 0, 0)

        return max_cost_value