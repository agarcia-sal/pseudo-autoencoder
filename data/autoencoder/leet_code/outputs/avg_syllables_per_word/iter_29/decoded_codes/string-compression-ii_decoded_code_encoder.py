from math import inf
from functools import lru_cache

class Solution:
    def getLengthOfOptimalCompression(self, s: str, k: int) -> int:
        @lru_cache(None)
        def dp(i: int, k_left: int, prev_char: str, prev_count: int) -> int:
            if k_left < 0:
                return inf
            if i == len(s):
                return 0
            curr_char = s[i]
            if curr_char == prev_char:
                increment = 1 if prev_count in (1, 9, 99) else 0
                return increment + dp(i + 1, k_left, prev_char, prev_count + 1)
            else:
                keep = 1 + dp(i + 1, k_left, curr_char, 1)
                delete = dp(i + 1, k_left - 1, prev_char, prev_count)
                return min(keep, delete)

        return dp(0, k, '', 0)