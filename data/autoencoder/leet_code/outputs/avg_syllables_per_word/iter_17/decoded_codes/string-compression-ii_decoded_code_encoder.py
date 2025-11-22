from functools import lru_cache
from math import inf

class Solution:
    def getLengthOfOptimalCompression(self, string_s: str, integer_k: int) -> int:
        @lru_cache(None)
        def dp(integer_i: int, integer_k: int, prev_char: str, prev_count: int) -> int:
            if integer_k < 0:
                return inf
            if integer_i == len(string_s):
                return 0

            current_char = string_s[integer_i]
            if current_char == prev_char:
                increment_value = 1 if prev_count in (1, 9, 99) else 0
                return increment_value + dp(integer_i + 1, integer_k, prev_char, prev_count + 1)
            else:
                keep_option = 1 + dp(integer_i + 1, integer_k, current_char, 1)
                delete_option = dp(integer_i + 1, integer_k - 1, prev_char, prev_count)
                return min(keep_option, delete_option)

        return dp(0, integer_k, "", 0)