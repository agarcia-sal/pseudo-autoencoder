class Solution:
    def new21Game(self, n: int, k: int, maxPts: int) -> float:
        from functools import lru_cache

        @lru_cache(None)
        def dfs(i):
            if i >= k:
                return 1.0 if i <= n else 0.0
            if i == k - 1:
                return min(n - k + 1, maxPts) / maxPts
            first_dfs = dfs(i + 1)
            second_dfs = dfs(i + maxPts + 1)
            return first_dfs + (first_dfs - second_dfs) / maxPts

        return dfs(0)