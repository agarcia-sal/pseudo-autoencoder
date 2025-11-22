from functools import lru_cache
from math import inf

class Solution:
    def getLengthOfOptimalCompression(self, s: str, k: int) -> int:
        @lru_cache(None)
        def dp(i: int, k: int, prev_char: str, prev_count: int) -> int:
            if k < 0:
                return inf
            if i == len(s):
                return 0

            current_char = s[i]
            if current_char == prev_char:
                # Increment length if prev_count is 1, 9, or 99 (number of digits increases)
                increment = 1 if prev_count in (1,9,99) else 0
                return increment + dp(i + 1, k, prev_char, prev_count + 1)
            else:
                # Option 1: keep current char as start of new group
                keep = 1 + dp(i + 1, k, current_char, 1)
                # Option 2: delete current char
                delete = dp(i + 1, k - 1, prev_char, prev_count)
                return min(keep, delete)

        return dp(0, k, '', 0)