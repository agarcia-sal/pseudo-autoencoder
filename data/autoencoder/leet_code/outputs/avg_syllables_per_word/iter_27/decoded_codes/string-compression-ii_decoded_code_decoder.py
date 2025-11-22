from math import inf
from functools import lru_cache

class Solution:
    def getLengthOfOptimalCompression(self, s: str, k: int) -> int:
        @lru_cache(None)
        def dp(i: int, k_value: int, prev_char: str, prev_count: int) -> int:
            if k_value < 0:
                return inf
            if i == len(s):
                return 0

            current_char = s[i]
            if current_char == prev_char:
                increment = 1 if prev_count in {1, 9, 99} else 0
                return increment + dp(i + 1, k_value, prev_char, prev_count + 1)
            else:
                keep = 1 + dp(i + 1, k_value, current_char, 1)
                delete = dp(i + 1, k_value - 1, prev_char, prev_count)
                return min(keep, delete)

        return dp(0, k, "", 0)