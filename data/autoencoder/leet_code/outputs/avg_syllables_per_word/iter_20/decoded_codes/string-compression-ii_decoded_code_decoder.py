import math
from functools import lru_cache

class Solution:
    def getLengthOfOptimalCompression(self, s: str, k: int) -> int:
        @lru_cache(None)
        def dp(i: int, k_value: int, prev_char: str, prev_count: int) -> int:
            if k_value < 0:
                return math.inf
            if i == len(s):
                return 0
            if s[i] == prev_char:
                increment = 0
                # increment count if counts hit 1, 9, or 99 (i.e. length changes from 1->2, 9->10, 99->100)
                if prev_count == 1 or prev_count == 9 or prev_count == 99:
                    increment = 1
                return increment + dp(i + 1, k_value, prev_char, prev_count + 1)
            else:
                keep_option = 1 + dp(i + 1, k_value, s[i], 1)
                delete_option = dp(i + 1, k_value - 1, prev_char, prev_count)
                return min(keep_option, delete_option)

        return dp(0, k, "", 0)