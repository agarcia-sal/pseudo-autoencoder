from functools import lru_cache

class Solution:
    def maxJumps(self, arr, d):
        n = len(arr)

        @lru_cache(None)
        def dp(i):
            max_jumps = 1
            for x in range(1, d + 1):
                ni = i + x
                if ni < n:
                    if arr[ni] >= arr[i]:
                        break
                    candidate = 1 + dp(ni)
                    if candidate > max_jumps:
                        max_jumps = candidate
                else:
                    break
            for x in range(1, d + 1):
                ni = i - x
                if ni >= 0:
                    if arr[ni] >= arr[i]:
                        break
                    candidate = 1 + dp(ni)
                    if candidate > max_jumps:
                        max_jumps = candidate
                else:
                    break
            return max_jumps

        results = [dp(i) for i in range(n)]
        return max(results)