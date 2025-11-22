from functools import lru_cache
from typing import List

class Solution:
    def maxJumps(self, arr: List[int], d: int) -> int:

        @lru_cache(None)
        def dp(i: int) -> int:
            max_jumps = 1
            n = len(arr)
            # Jump forward
            for x in range(1, d + 1):
                nxt = i + x
                if nxt >= n:
                    break
                if arr[nxt] >= arr[i]:
                    break
                possible_jumps = 1 + dp(nxt)
                if possible_jumps > max_jumps:
                    max_jumps = possible_jumps

            # Jump backward
            for x in range(1, d + 1):
                nxt = i - x
                if nxt < 0:
                    break
                if arr[nxt] >= arr[i]:
                    break
                possible_jumps = 1 + dp(nxt)
                if possible_jumps > max_jumps:
                    max_jumps = possible_jumps

            return max_jumps

        max_overall = 0
        for i in range(len(arr)):
            current_jumps = dp(i)
            if current_jumps > max_overall:
                max_overall = current_jumps
        return max_overall