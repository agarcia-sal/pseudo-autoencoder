from typing import List
from functools import lru_cache

class Solution:
    def maxJumps(self, arr: List[int], d: int) -> int:
        n = len(arr)

        @lru_cache(None)
        def dp(i: int) -> int:
            max_jumps = 1
            # Jump to the right
            for x in range(1, d + 1):
                if i + x >= n:
                    break
                if arr[i + x] >= arr[i]:
                    break
                candidate = 1 + dp(i + x)
                if candidate > max_jumps:
                    max_jumps = candidate
            # Jump to the left
            for x in range(1, d + 1):
                if i - x < 0:
                    break
                if arr[i - x] >= arr[i]:
                    break
                candidate = 1 + dp(i - x)
                if candidate > max_jumps:
                    max_jumps = candidate
            return max_jumps

        max_value = 0
        for i in range(n):
            current = dp(i)
            if current > max_value:
                max_value = current

        return max_value