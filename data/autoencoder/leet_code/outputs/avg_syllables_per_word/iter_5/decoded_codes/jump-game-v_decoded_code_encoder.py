from functools import lru_cache

class Solution:
    def maxJumps(self, arr, d):
        n = len(arr)

        @lru_cache(None)
        def dp(i):
            max_jumps = 1
            for x in range(1, d+1):
                if i + x >= n:
                    break
                if arr[i + x] >= arr[i]:
                    break
                max_jumps = max(max_jumps, 1 + dp(i + x))
            for x in range(1, d+1):
                if i - x < 0:
                    break
                if arr[i - x] >= arr[i]:
                    break
                max_jumps = max(max_jumps, 1 + dp(i - x))
            return max_jumps

        result = 0
        for i in range(n):
            result = max(result, dp(i))
        return result