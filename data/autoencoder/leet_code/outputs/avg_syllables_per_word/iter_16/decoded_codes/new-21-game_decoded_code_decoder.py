class Solution:
    def new21Game(self, n: int, k: int, maxPts: int) -> float:
        from functools import lru_cache

        @lru_cache(None)
        def dfs(i: int) -> float:
            if i >= k:
                return 1.0 if i <= n else 0.0
            if i == k - 1:
                diff = n - k + 1
                minimum_value = diff if diff < maxPts else maxPts
                return minimum_value / maxPts
            first_res = dfs(i + 1)
            second_res = dfs(i + maxPts + 1)
            numerator = first_res - second_res
            return first_res + numerator / maxPts

        return dfs(0)