from functools import lru_cache

class Solution:
    def new21Game(self, n: int, k: int, maxPts: int) -> float:
        @lru_cache(None)
        def dfs(i: int) -> float:
            if i >= k:
                return 1.0 if i <= n else 0.0
            if i == k - 1:
                difference = n - k + 1
                numerator = difference if difference < maxPts else maxPts
                return numerator / maxPts
            first_call = dfs(i + 1)
            second_call = dfs(i + maxPts + 1)
            recurrence_value = first_call + (first_call - second_call) / maxPts
            return recurrence_value
        return dfs(0)