from functools import lru_cache

class Solution:
    def new21Game(self, n: int, k: int, maxPts: int) -> float:
        @lru_cache(None)
        def dfs(i: int) -> float:
            if i >= k:
                return 1.0 if i <= n else 0.0
            if i == k - 1:
                return min(n - k + 1, maxPts) / maxPts
            # Using sliding window-like optimization inherent in the formula
            # dfs(i) = dfs(i+1) + (dfs(i+1) - dfs(i+maxPts+1)) / maxPts
            return dfs(i + 1) + (dfs(i + 1) - dfs(i + maxPts + 1)) / maxPts

        return dfs(0)