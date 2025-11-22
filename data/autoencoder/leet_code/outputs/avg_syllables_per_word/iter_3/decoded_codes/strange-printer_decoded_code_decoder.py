class Solution:
    def strangePrinter(self, s: str) -> int:
        from functools import lru_cache

        @lru_cache(None)
        def dp(i: int, j: int) -> int:
            if i > j:
                return 0
            result = dp(i, j - 1) + 1
            for k in range(i, j):
                if s[k] == s[j]:
                    result = min(result, dp(i, k - 1) + dp(k, j - 1))
            return result

        return dp(0, len(s) - 1)