from functools import lru_cache

class Solution:
    def maxJumps(self, arr, d):
        n = len(arr)

        @lru_cache(None)
        def dp(i):
            max_jumps = 1
            # jump right
            for x in range(1, d + 1):
                ni = i + x
                if ni >= n:
                    break
                if arr[ni] >= arr[i]:
                    break
                max_jumps = max(max_jumps, 1 + dp(ni))
            # jump left
            for x in range(1, d + 1):
                ni = i - x
                if ni < 0:
                    break
                if arr[ni] >= arr[i]:
                    break
                max_jumps = max(max_jumps, 1 + dp(ni))
            return max_jumps

        maximum_result = 0
        for i in range(n):
            maximum_result = max(maximum_result, dp(i))
        return maximum_result