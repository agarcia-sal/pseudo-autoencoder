class Solution:
    def strangePrinter(self, s: str) -> int:
        from functools import lru_cache

        n = len(s)

        @lru_cache(None)
        def dp(i: int, j: int) -> int:
            if i > j:
                return 0
            result = dp(i, j - 1) + 1
            for k in range(i, j):
                if s[k] == s[j]:
                    temp_result = dp(i, k) + dp(k + 1, j - 1)
                    if temp_result < result:
                        result = temp_result
            return result

        return dp(0, n - 1)