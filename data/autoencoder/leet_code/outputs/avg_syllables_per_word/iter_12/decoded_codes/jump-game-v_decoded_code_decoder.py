class Solution:
    def maxJumps(self, arr, d):
        from functools import lru_cache

        n = len(arr)

        @lru_cache(None)
        def dp(i):
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

        maximum_jumps = 0
        for i in range(n):
            current_jumps = dp(i)
            if current_jumps > maximum_jumps:
                maximum_jumps = current_jumps
        return maximum_jumps