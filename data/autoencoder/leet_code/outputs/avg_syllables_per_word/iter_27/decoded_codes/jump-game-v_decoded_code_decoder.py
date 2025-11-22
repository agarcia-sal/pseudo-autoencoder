from typing import List
from functools import lru_cache

class Solution:
    def maxJumps(self, arr: List[int], d: int) -> int:
        n = len(arr)

        @lru_cache(None)
        def dp(i: int) -> int:
            max_jumps = 1
            # jump to the right
            for x in range(1, d + 1):
                j = i + x
                if j >= n:
                    break
                if arr[j] >= arr[i]:
                    break
                candidate_jumps = 1 + dp(j)
                if candidate_jumps > max_jumps:
                    max_jumps = candidate_jumps
            # jump to the left
            for x in range(1, d + 1):
                j = i - x
                if j < 0:
                    break
                if arr[j] >= arr[i]:
                    break
                candidate_jumps = 1 + dp(j)
                if candidate_jumps > max_jumps:
                    max_jumps = candidate_jumps
            return max_jumps

        max_result = 0
        for i in range(n):
            current_result = dp(i)
            if current_result > max_result:
                max_result = current_result
        return max_result