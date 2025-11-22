class Solution:
    def new21Game(self, n: int, k: int, maxPts: int) -> float:
        from functools import lru_cache

        @lru_cache(None)
        def dfs(i: int) -> float:
            if i >= k:
                return 1.0 if i <= n else 0.0
            if i == k - 1:
                prob = min(n - k + 1, maxPts) / maxPts
                return prob
            value_next = dfs(i + 1)
            value_further = dfs(i + maxPts + 1)
            result = value_next + (value_next - value_further) / maxPts
            return result

        return dfs(0)