from functools import lru_cache
from typing import List

class Solution:
    def maxJumps(self, arr: List[int], d: int) -> int:
        n = len(arr)

        @lru_cache(None)
        def dp(i: int) -> int:
            max_jumps = 1
            # Jump forward
            for x in range(1, d + 1):
                ni = i + x
                if ni >= n:
                    break
                if arr[ni] >= arr[i]:
                    break
                max_jumps = max(max_jumps, 1 + dp(ni))
            # Jump backward
            for x in range(1, d + 1):
                ni = i - x
                if ni < 0:
                    break
                if arr[ni] >= arr[i]:
                    break
                max_jumps = max(max_jumps, 1 + dp(ni))
            return max_jumps

        return max(dp(i) for i in range(n))