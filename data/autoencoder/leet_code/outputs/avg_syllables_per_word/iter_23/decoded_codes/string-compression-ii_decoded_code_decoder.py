from functools import lru_cache
import math

class Solution:
    def getLengthOfOptimalCompression(self, s: str, k: int) -> int:
        @lru_cache(None)
        def dp(i: int, k_remaining: int, prev_char: str, prev_count: int) -> int:
            if k_remaining < 0:
                return math.inf
            if i == len(s):
                return 0
            current_char = s[i]
            if current_char == prev_char:
                # increment length if prev_count is 1, 9, or 99 (thresholds where compressed length increases)
                increment = 1 if prev_count in {1, 9, 99} else 0
                return increment + dp(i + 1, k_remaining, prev_char, prev_count + 1)
            else:
                # Option 1: keep current char, which adds at least length 1
                keep = 1 + dp(i + 1, k_remaining, current_char, 1)
                # Option 2: delete current char (if we have deletions left)
                delete = dp(i + 1, k_remaining - 1, prev_char, prev_count)
                return min(keep, delete)
        return dp(0, k, '', 0)