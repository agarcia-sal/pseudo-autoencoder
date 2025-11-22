class Solution:
    def new21Game(self, n: int, k: int, maxPts: int) -> float:
        from functools import lru_cache

        @lru_cache(None)
        def dfs(i: int) -> float:
            if i >= k:
                return 1.0 if i <= n else 0.0
            if i == k - 1:
                return min(n - k + 1, maxPts) / maxPts
            first_call = dfs(i + 1)
            second_call = dfs(i + maxPts + 1)
            difference = first_call - second_call
            return first_call + difference / maxPts

        return dfs(0)