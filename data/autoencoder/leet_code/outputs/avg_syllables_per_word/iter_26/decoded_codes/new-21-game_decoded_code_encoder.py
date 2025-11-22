class Solution:
    def new21Game(self, n: int, k: int, maxPts: int) -> float:
        from functools import lru_cache

        @lru_cache(None)
        def dfs(i: int) -> float:
            if i >= k:
                return float(i <= n)
            if i == k - 1:
                return min(n - k + 1, maxPts) / maxPts
            # Probability is average of next maxPts probabilities
            total = 0.0
            for x in range(1, maxPts + 1):
                total += dfs(i + x)
            return total / maxPts

        return dfs(0)