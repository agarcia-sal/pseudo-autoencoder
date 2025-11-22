class Solution:
    def new21Game(self, n, k, maxPts):
        from functools import lru_cache

        @lru_cache(None)
        def dfs(i):
            if i >= k:
                return 1 if i <= n else 0
            if i == k - 1:
                value = min(n - k + 1, maxPts) / maxPts
                return value
            return dfs(i + 1) + (dfs(i + 1) - dfs(i + maxPts + 1)) / maxPts

        return dfs(0)