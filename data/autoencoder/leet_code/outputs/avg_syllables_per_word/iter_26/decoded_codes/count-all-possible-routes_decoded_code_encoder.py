class Solution:
    def countRoutes(self, locations, start, finish, fuel):
        MODULO_VALUE = 10**9 + 7
        number_of_locations = len(locations)

        from functools import lru_cache

        @lru_cache(None)
        def dp(city, remaining_fuel):
            if remaining_fuel < 0:
                return 0

            routes = 1 if city == finish else 0

            for next_city in range(number_of_locations):
                if next_city != city:
                    fuel_cost = abs(locations[city] - locations[next_city])
                    if remaining_fuel >= fuel_cost:
                        routes = (routes + dp(next_city, remaining_fuel - fuel_cost)) % MODULO_VALUE

            return routes

        return dp(start, fuel)