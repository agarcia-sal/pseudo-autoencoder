from functools import lru_cache
import math

class Solution:
    def getLengthOfOptimalCompression(self, s: str, k: int) -> int:
        @lru_cache(None)
        def dp(i: int, k_remaining: int, previous_character: str, previous_count: int) -> int:
            if k_remaining < 0:
                return math.inf
            if i == len(s):
                return 0

            current_char = s[i]
            if current_char == previous_character:
                increment_value = 1 if previous_count in (1, 9, 99) else 0
                return increment_value + dp(i + 1, k_remaining, previous_character, previous_count + 1)
            else:
                keep_option = 1 + dp(i + 1, k_remaining, current_char, 1)
                delete_option = dp(i + 1, k_remaining - 1, previous_character, previous_count)
                return min(keep_option, delete_option)

        return dp(0, k, "", 0)