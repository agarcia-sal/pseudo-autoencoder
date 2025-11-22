class Solution:
    def maxJumps(self, arr, d):
        from functools import lru_cache

        n = len(arr)

        @lru_cache(None)
        def dp(i):
            max_jumps = 1
            # jump to the right
            for x in range(1, d + 1):
                if i + x >= n:
                    break
                if arr[i + x] >= arr[i]:
                    break
                max_jumps = max(max_jumps, 1 + dp(i + x))
            # jump to the left
            for x in range(1, d + 1):
                if i - x < 0:
                    break
                if arr[i - x] >= arr[i]:
                    break
                max_jumps = max(max_jumps, 1 + dp(i - x))
            return max_jumps

        return max(dp(i) for i in range(n))