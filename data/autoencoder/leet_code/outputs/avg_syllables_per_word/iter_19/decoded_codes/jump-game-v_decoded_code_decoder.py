from functools import lru_cache

class Solution:
    def maxJumps(self, arr, d):
        n = len(arr)

        @lru_cache(None)
        def dp(i):
            max_jumps = 1
            # Jump right
            for x in range(1, d + 1):
                j = i + x
                if j >= n:
                    break
                if arr[j] >= arr[i]:
                    break
                max_jumps = max(max_jumps, 1 + dp(j))
            # Jump left
            for x in range(1, d + 1):
                j = i - x
                if j < 0:
                    break
                if arr[j] >= arr[i]:
                    break
                max_jumps = max(max_jumps, 1 + dp(j))
            return max_jumps

        return max(dp(i) for i in range(n))