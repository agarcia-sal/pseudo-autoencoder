from functools import cache

class Solution:
    def maxJumps(self, arr, d):
        n = len(arr)

        @cache
        def dp(i):
            max_jumps = 1
            for x in range(1, d + 1):
                if i + x < n:
                    if arr[i + x] >= arr[i]:
                        break
                    max_jumps = max(max_jumps, 1 + dp(i + x))
                else:
                    break
            for x in range(1, d + 1):
                if i - x >= 0:
                    if arr[i - x] >= arr[i]:
                        break
                    max_jumps = max(max_jumps, 1 + dp(i - x))
                else:
                    break
            return max_jumps

        return max(dp(i) for i in range(n))