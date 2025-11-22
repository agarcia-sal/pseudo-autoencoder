from functools import lru_cache

class Solution:
    def getLengthOfOptimalCompression(self, s: str, k: int) -> int:
        @lru_cache(None)
        def dp(i: int, k_remaining: int, previous_character: str, previous_count: int) -> int:
            if k_remaining < 0:
                return float('inf')
            if i == len(s):
                return 0
            if s[i] == previous_character:
                increment = 1 if previous_count in (1, 9, 99) else 0
                return increment + dp(i + 1, k_remaining, previous_character, previous_count + 1)
            else:
                keep_length = 1 + dp(i + 1, k_remaining, s[i], 1)
                delete_length = dp(i + 1, k_remaining - 1, previous_character, previous_count)
                return min(keep_length, delete_length)

        return dp(0, k, '', 0)