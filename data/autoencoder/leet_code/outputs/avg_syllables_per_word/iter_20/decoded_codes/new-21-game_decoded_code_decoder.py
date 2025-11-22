class Solution:
    def new21Game(self, n: int, k: int, maxPts: int) -> float:
        from functools import lru_cache

        @lru_cache(None)
        def dfs(i: int) -> float:
            if i >= k:
                return 1.0 if i <= n else 0.0
            if i == k - 1:
                minimum_value = min(n - k + 1, maxPts)
                probability = minimum_value / maxPts
                return probability
            first_recursive_call = dfs(i + 1)
            second_recursive_call = dfs(i + maxPts + 1)
            result = first_recursive_call + (first_recursive_call - second_recursive_call) / maxPts
            return result

        return dfs(0)