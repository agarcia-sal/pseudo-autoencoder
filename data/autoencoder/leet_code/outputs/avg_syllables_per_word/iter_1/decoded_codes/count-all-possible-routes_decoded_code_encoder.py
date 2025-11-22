MOD = 10**9 + 7

def count_routes(locations, start, finish, fuel):
    n = len(locations)

    from functools import lru_cache

    @lru_cache(None)
    def dp(city, fuel_left):
        if fuel_left < 0:
            return 0
        routes = 1 if city == finish else 0
        for next_city in range(n):
            if next_city != city:
                cost = abs(locations[city] - locations[next_city])
                if fuel_left >= cost:
                    routes = (routes + dp(next_city, fuel_left - cost)) % MOD
        return routes

    return dp(start, fuel)