class Solution:
    def new21Game(self, n: int, k: int, maxPts: int) -> float:
        from functools import lru_cache

        @lru_cache(None)
        def dfs(i: int) -> float:
            if i >= k:
                return 1.0 if i <= n else 0.0
            if i == k - 1:
                numerator = min(n - k + 1, maxPts)
                return numerator / maxPts
            result = dfs(i + 1) + (dfs(i + 1) - dfs(i + maxPts + 1)) / maxPts
            return result

        return dfs(0)