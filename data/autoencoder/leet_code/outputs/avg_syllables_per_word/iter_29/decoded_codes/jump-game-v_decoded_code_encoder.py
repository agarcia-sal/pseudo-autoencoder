from functools import lru_cache

class Solution:
    def maxJumps(self, arr: list[int], d: int) -> int:
        n = len(arr)

        @lru_cache(None)
        def dp(i: int) -> int:
            max_jumps = 1
            # Jump forward
            for x in range(1, d + 1):
                j = i + x
                if j >= n:
                    break
                if arr[j] >= arr[i]:
                    break
                max_jumps = max(max_jumps, 1 + dp(j))
            # Jump backward
            for x in range(1, d + 1):
                j = i - x
                if j < 0:
                    break
                if arr[j] >= arr[i]:
                    break
                max_jumps = max(max_jumps, 1 + dp(j))
            return max_jumps

        return max(dp(i) for i in range(n))