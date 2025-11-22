class Solution:
    def new21Game(self, n: int, k: int, maxPts: int) -> float:
        from functools import lru_cache

        @lru_cache(None)
        def dfs(i: int) -> float:
            if i >= k:
                return 1.0 if i <= n else 0.0
            if i == k - 1:
                difference = n - k + 1
                numerator = maxPts if difference > maxPts else difference
                return numerator / maxPts
            value1 = dfs(i + 1)
            value2 = dfs(i + maxPts + 1)
            difference = value1 - value2
            return value1 + difference / maxPts

        return dfs(0)