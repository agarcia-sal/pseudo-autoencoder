from functools import cache

class Solution:
    def countRoutes(self, locations: list[int], start: int, finish: int, fuel: int) -> int:
        MOD = 10**9 + 7
        n = len(locations)

        @cache
        def dp(city: int, remaining_fuel: int) -> int:
            if remaining_fuel < 0:
                return 0
            routes = 1 if city == finish else 0
            for next_city in range(n):
                if next_city != city:
                    fuel_cost = abs(locations[city] - locations[next_city])
                    if remaining_fuel >= fuel_cost:
                        routes = (routes + dp(next_city, remaining_fuel - fuel_cost)) % MOD
            return routes

        return dp(start, fuel)