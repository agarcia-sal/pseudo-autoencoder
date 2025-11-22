from typing import List
from functools import lru_cache

class Solution:
    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:
        MODULO = 10**9 + 7
        number_of_locations = len(locations)

        @lru_cache(None)
        def dp(city: int, remaining_fuel: int) -> int:
            if remaining_fuel < 0:
                return 0
            total_routes = 1 if city == finish else 0
            for next_city in range(number_of_locations):
                if next_city != city:
                    fuel_cost = abs(locations[city] - locations[next_city])
                    if remaining_fuel >= fuel_cost:
                        total_routes = (total_routes + dp(next_city, remaining_fuel - fuel_cost)) % MODULO
            return total_routes

        return dp(start, fuel)