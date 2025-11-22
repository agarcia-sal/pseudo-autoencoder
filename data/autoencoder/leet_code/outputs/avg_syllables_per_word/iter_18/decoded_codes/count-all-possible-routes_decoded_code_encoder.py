class Solution:
    def countRoutes(self, locations, start, finish, fuel):
        MOD = 10**9 + 1
        n = len(locations)
        memo = {}

        def dp(city, remaining_fuel):
            if remaining_fuel < 0:
                return 0
            if (city, remaining_fuel) in memo:
                return memo[(city, remaining_fuel)]
            routes = 1 if city == finish else 0
            for next_city in range(n):
                if next_city != city:
                    cost = abs(locations[city] - locations[next_city])
                    if remaining_fuel >= cost:
                        routes = (routes + dp(next_city, remaining_fuel - cost)) % MOD
            memo[(city, remaining_fuel)] = routes
            return routes

        return dp(start, fuel)