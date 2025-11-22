from functools import lru_cache
from typing import List

class Solution:
    def maxJumps(self, arr: List[int], d: int) -> int:
        n = len(arr)

        @lru_cache(None)
        def dp(i: int) -> int:
            max_jumps = 1
            for x in range(1, d + 1):
                if i + x < n:
                    if arr[i + x] >= arr[i]:
                        break
                    max_jumps = max(max_jumps, 1 + dp(i + x))
            for x in range(1, d + 1):
                if i - x >= 0:
                    if arr[i - x] >= arr[i]:
                        break
                    max_jumps = max(max_jumps, 1 + dp(i - x))
            return max_jumps

        return max(dp(i) for i in range(n))