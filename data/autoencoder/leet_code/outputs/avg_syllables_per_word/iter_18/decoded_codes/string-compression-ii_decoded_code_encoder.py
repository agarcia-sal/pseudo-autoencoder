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

            c = s[i]
            if c == prev_char:
                increment = 0
                # Increment length if prev_count in {1,9,99} because "a", "a9", and "a99" each increase length when count increases.
                if prev_count in {1, 9, 99}:
                    increment = 1
                return increment + dp(i + 1, k, prev_char, prev_count + 1)
            else:
                keep = 1 + dp(i + 1, k, c, 1)
                delete = dp(i + 1, k - 1, prev_char, prev_count)
                return min(keep, delete)

        return dp(0, k, '', 0)