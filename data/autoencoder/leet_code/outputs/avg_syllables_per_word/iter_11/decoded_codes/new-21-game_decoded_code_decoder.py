from functools import cache

class Solution:
    def new21Game(self, n: int, k: int, maxPts: int) -> float:
        @cache
        def dfs(i: int) -> float:
            if i >= k:
                return float(i <= n)
            if i == k - 1:
                return min(n - k + 1, maxPts) / maxPts
            result = dfs(i + 1) + (dfs(i + 1) - dfs(i + maxPts + 1)) / maxPts
            return result
        return dfs(0)