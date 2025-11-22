class Solution:
    def new21Game(self, n: int, k: int, maxPts: int) -> float:
        from functools import lru_cache

        @lru_cache(None)
        def dfs(i: int) -> float:
            if i >= k:
                return 1.0 if i <= n else 0.0
            if i == k - 1:
                minimum_value = min(n - k + 1, maxPts)
                return minimum_value / maxPts
            first_call = dfs(i + 1)
            second_call = dfs(i + maxPts + 1)
            return first_call + (first_call - second_call) / maxPts

        return dfs(0)