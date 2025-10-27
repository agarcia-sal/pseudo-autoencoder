class Solution:
    def new21Game(self, n: int, k: int, maxPts: int) -> float:
        zero, one = 0.0, 1.0

        from functools import lru_cache

        @lru_cache(None)
        def dfs(i: int) -> float:
            if i >= k:
                return one if i <= n else zero
            if i == k - 1:
                val = n - k + 1
                return (val / maxPts) if val < maxPts else one
            first_call = dfs(i + 1)
            second_call = dfs(i + maxPts + 1)
            result = first_call + (first_call - second_call) / maxPts
            return result

        return dfs(0)