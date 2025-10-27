from math import inf
from functools import lru_cache

class Solution:
    def getLengthOfOptimalCompression(self, s: str, k: int) -> int:
        @lru_cache(None)
        def dp(i: int, k: int, prev_char: str, prev_count: int) -> int:
            if k < 0:
                return inf
            if i == len(s):
                return 0

            curr_char = s[i]
            if curr_char == prev_char:
                # Increment length only when count changes the compressed length representation:
                # when count is 1, 9, or 99 (since counts like 2-9 have single digit length, 10-99 two digits, etc.)
                increment = 1 if prev_count in {1, 9, 99} else 0
                return increment + dp(i + 1, k, prev_char, prev_count + 1)
            else:
                keep = 1 + dp(i + 1, k, curr_char, 1)  # Keep current char as new sequence
                delete = dp(i + 1, k - 1, prev_char, prev_count)  # Delete current char
                return min(keep, delete)

        return dp(0, k, '', 0)