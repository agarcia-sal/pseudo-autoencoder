from functools import lru_cache

class Solution:
    def new21Game(self, n: int, k: int, maxPts: int) -> float:
        @lru_cache(None)
        def dfs(i: int) -> float:
            if i >= k:
                return 1.0 if i <= n else 0.0
            if i == k - 1:
                numerator = n - k + 1
                if numerator > maxPts:
                    numerator = maxPts
                return numerator / maxPts
            first_term = dfs(i + 1)
            second_term = dfs(i + 1) - dfs(i + maxPts + 1)
            return first_term + second_term / maxPts
        return dfs(0)