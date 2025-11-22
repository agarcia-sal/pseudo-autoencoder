from typing import List

class Solution:
    def maxJumps(self, arr: List[int], d: int) -> int:
        from functools import lru_cache

        n = len(arr)

        @lru_cache(None)
        def dp(i: int) -> int:
            max_jumps = 1
            for x in range(1, d + 1):
                j = i + x
                if j < n:
                    if arr[j] >= arr[i]:
                        break
                    max_jumps = max(max_jumps, 1 + dp(j))
                else:
                    break
            for x in range(1, d + 1):
                j = i - x
                if j >= 0:
                    if arr[j] >= arr[i]:
                        break
                    max_jumps = max(max_jumps, 1 + dp(j))
                else:
                    break
            return max_jumps

        return max(dp(i) for i in range(n))