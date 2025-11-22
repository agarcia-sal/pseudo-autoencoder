class Solution:
    def new21Game(self, n: int, k: int, maxPts: int) -> float:
        from functools import lru_cache

        @lru_cache(None)
        def dfs(i: int) -> float:
            if i >= k:
                return 1.0 if i <= n else 0.0
            elif i == k - 1:
                diff = n - k + 1
                numerator = diff if diff < maxPts else maxPts
                return numerator / maxPts
            else:
                value1 = dfs(i + 1)
                value2 = dfs(i + maxPts + 1)
                numerator2 = value1 - value2
                part2 = numerator2 / maxPts
                return value1 + part2

        return dfs(0)