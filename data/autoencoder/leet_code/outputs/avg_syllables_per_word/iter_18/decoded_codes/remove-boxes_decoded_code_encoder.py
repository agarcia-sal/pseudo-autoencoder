from functools import lru_cache
from typing import List, Dict, Tuple

class Solution:
    def removeBoxes(self, boxes: List[int]) -> int:
        from sys import setrecursionlimit
        setrecursionlimit(10**7)

        @lru_cache(None)
        def dp(l: int, r: int, k: int) -> int:
            if l > r:
                return 0

            # Optimization: combine continuous boxes of the same color at the end
            while r > l and boxes[r] == boxes[r - 1]:
                r -= 1
                k += 1

            # Base removal: remove boxes[r] with k+1 same boxes directly
            res = dp(l, r - 1, 0) + (k + 1) * (k + 1)

            for i in range(l, r):
                if boxes[i] == boxes[r]:
                    candidate_result = dp(l, i, k + 1) + dp(i + 1, r - 1, 0)
                    if candidate_result > res:
                        res = candidate_result
            return res

        return dp(0, len(boxes) - 1, 0)