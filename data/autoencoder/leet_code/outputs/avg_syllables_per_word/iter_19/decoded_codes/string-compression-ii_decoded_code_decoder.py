from math import inf
from functools import lru_cache

class Solution:
    def getLengthOfOptimalCompression(self, s, k):
        @lru_cache(None)
        def dp(i, k_left, prev_char, prev_count):
            if k_left < 0:
                return inf
            if i == len(s):
                return 0
            cur_char = s[i]
            if cur_char == prev_char:
                # Increment cost only when count changes length in compressed form
                increment = 1 if prev_count in (1, 9, 99) else 0
                return increment + dp(i + 1, k_left, prev_char, prev_count + 1)
            else:
                # Keep current char (starts count = 1)
                keep = 1 + dp(i + 1, k_left, cur_char, 1)
                # Delete current char (use one from k_left)
                delete = dp(i + 1, k_left - 1, prev_char, prev_count)
                return min(keep, delete)

        return dp(0, k, '', 0)