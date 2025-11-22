from math import inf
from functools import lru_cache

class Solution:
    def getLengthOfOptimalCompression(self, s: str, k: int) -> int:
        n = len(s)

        @lru_cache(None)
        def dp(i: int, k_remaining: int, prev_char: str, prev_count: int) -> int:
            if k_remaining < 0:
                return inf
            if i == n:
                return 0

            curr_char = s[i]

            if curr_char == prev_char:
                increment = 0
                if prev_count in (1, 9, 99):
                    increment = 1
                return increment + dp(i + 1, k_remaining, prev_char, prev_count + 1)
            else:
                keep = 1 + dp(i + 1, k_remaining, curr_char, 1)
                delete = dp(i + 1, k_remaining - 1, prev_char, prev_count)
                return min(keep, delete)

        return dp(0, k, '', 0)