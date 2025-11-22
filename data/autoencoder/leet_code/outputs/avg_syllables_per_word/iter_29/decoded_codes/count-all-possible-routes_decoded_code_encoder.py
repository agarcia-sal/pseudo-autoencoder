from functools import lru_cache

class Solution:
    def countRoutes(self, locations: list[int], start: int, finish: int, fuel: int) -> int:
        MODULO_VALUE = 10**9 + 7
        number_of_locations = len(locations)

        @lru_cache(None)
        def dp(city: int, remaining_fuel: int) -> int:
            if remaining_fuel < 0:
                return 0
            route_count = 1 if city == finish else 0
            for next_city in range(number_of_locations):
                if next_city != city:
                    fuel_cost = abs(locations[city] - locations[next_city])
                    if remaining_fuel >= fuel_cost:
                        route_count = (route_count + dp(next_city, remaining_fuel - fuel_cost)) % MODULO_VALUE
            return route_count

        return dp(start, fuel)