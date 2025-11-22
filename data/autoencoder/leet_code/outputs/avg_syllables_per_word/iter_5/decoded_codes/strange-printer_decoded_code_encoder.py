class Solution:
    def strangePrinter(self, s: str) -> int:
        from functools import lru_cache

        @lru_cache(None)
        def dp(i, j):
            if i > j:
                return 0
            result = dp(i, j - 1) + 1
            for k in range(i, j):
                if s[k] == s[j]:
                    candidate = dp(i, k - 1) + dp(k, j - 1)
                    if candidate < result:
                        result = candidate
            return result

        return dp(0, len(s) - 1)