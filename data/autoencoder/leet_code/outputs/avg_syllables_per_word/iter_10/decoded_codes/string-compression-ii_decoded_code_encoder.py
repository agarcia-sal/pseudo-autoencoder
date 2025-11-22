class Solution:
    def getLengthOfOptimalCompression(self, s: str, k: int) -> int:
        from functools import lru_cache
        n = len(s)

        @lru_cache(None)
        def dp(i, k_remaining, prev_char, prev_count):
            if k_remaining < 0:
                return float('inf')
            if i == n:
                return 0

            if s[i] == prev_char:
                increment = 1 if prev_count in {1, 9, 99} else 0
                return increment + dp(i + 1, k_remaining, prev_char, prev_count + 1)
            else:
                keep = 1 + dp(i + 1, k_remaining, s[i], 1)
                delete = dp(i + 1, k_remaining - 1, prev_char, prev_count)
                return min(keep, delete)

        return dp(0, k, '', 0)