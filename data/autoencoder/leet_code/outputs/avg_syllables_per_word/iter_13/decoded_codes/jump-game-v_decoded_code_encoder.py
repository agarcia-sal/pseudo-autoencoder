from functools import lru_cache
from typing import List

class Solution:
    def maxJumps(self, arr: List[int], d: int) -> int:
        n = len(arr)

        @lru_cache(None)
        def dp(i: int) -> int:
            max_jumps = 1
            # Jump to the right
            for x in range(1, d + 1):
                j = i + x
                if j >= n:
                    break
                if arr[j] >= arr[i]:
                    break
                max_jumps = max(max_jumps, 1 + dp(j))
            # Jump to the left
            for x in range(1, d + 1):
                j = i - x
                if j < 0:
                    break
                if arr[j] >= arr[i]:
                    break
                max_jumps = max(max_jumps, 1 + dp(j))
            return max_jumps

        return max(dp(i) for i in range(n))