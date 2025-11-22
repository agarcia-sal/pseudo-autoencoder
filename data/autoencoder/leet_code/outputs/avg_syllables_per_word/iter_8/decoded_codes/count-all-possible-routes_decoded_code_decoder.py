class Solution:
    def countRoutes(self, locations, start, finish, fuel):
        MOD = 10**9 + 7
        n = len(locations)

        from functools import lru_cache

        @lru_cache(None)
        def dp(city, remaining_fuel):
            if remaining_fuel < 0:
                return 0

            routes = 0
            if city == finish:
                routes = 1

            for next_city in range(n):
                if next_city != city:
                    fuel_cost = abs(locations[city] - locations[next_city])
                    if remaining_fuel >= fuel_cost:
                        routes = (routes + dp(next_city, remaining_fuel - fuel_cost)) % MOD

            return routes

        return dp(start, fuel)