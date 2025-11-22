from functools import lru_cache

class Solution:
    def maxJumps(self, arr: list[int], d: int) -> int:
        n = len(arr)

        @lru_cache(None)
        def dp(i: int) -> int:
            max_jumps = 1
            for x in range(1, d + 1):
                if i + x >= n:
                    break
                if arr[i + x] >= arr[i]:
                    break
                candidate_jumps = 1 + dp(i + x)
                if candidate_jumps > max_jumps:
                    max_jumps = candidate_jumps
            for x in range(1, d + 1):
                if i - x < 0:
                    break
                if arr[i - x] >= arr[i]:
                    break
                candidate_jumps = 1 + dp(i - x)
                if candidate_jumps > max_jumps:
                    max_jumps = candidate_jumps
            return max_jumps

        maximum_overall = 0
        for i in range(n):
            current_jumps = dp(i)
            if current_jumps > maximum_overall:
                maximum_overall = current_jumps
        return maximum_overall