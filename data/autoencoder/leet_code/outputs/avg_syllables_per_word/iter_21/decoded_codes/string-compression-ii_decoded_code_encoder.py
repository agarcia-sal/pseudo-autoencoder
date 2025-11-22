from math import inf
from functools import lru_cache

class Solution:
    def getLengthOfOptimalCompression(self, s: str, k: int) -> int:
        @lru_cache(None)
        def dp(i: int, k_parameter: int, prev_char: str, prev_count: int) -> int:
            if k_parameter < 0:
                return inf
            if i == len(s):
                return 0
            if s[i] == prev_char:
                increment = 1 if prev_count in {1, 9, 99} else 0
                return increment + dp(i + 1, k_parameter, prev_char, prev_count + 1)
            else:
                keep = 1 + dp(i + 1, k_parameter, s[i], 1)
                delete = dp(i + 1, k_parameter - 1, prev_char, prev_count)
                return min(keep, delete)

        return dp(0, k, '', 0)