class Solution:
    def countRoutes(self, locations, start, finish, fuel):
        MOD = 10**9 + 1
        n = len(locations)
        from functools import lru_cache

        @lru_cache(None)
        def dp(city, remaining_fuel):
            if remaining_fuel < 0:
                return 0
            routes = 1 if city == finish else 0
            for next_city in range(n):
                if next_city != city:
                    fuel_cost = abs(locations[city] - locations[next_city])
                    if remaining_fuel >= fuel_cost:
                        routes += dp(next_city, remaining_fuel - fuel_cost)
                        routes %= MOD
            return routes

        return dp(start, fuel)