from functools import lru_cache
from typing import List

class Solution:
    def removeBoxes(self, boxes: List[int]) -> int:
        n = len(boxes)

        @lru_cache(None)
        def dp(l: int, r: int, k: int) -> int:
            if l > r:
                return 0
            # Optimize by merging boxes of the same color at the end
            while r > l and boxes[r] == boxes[r - 1]:
                r -= 1
                k += 1
            # Remove boxes[r] plus k same-colored boxes appended to it
            res = dp(l, r - 1, 0) + (k + 1) * (k + 1)
            for i in range(l, r):
                if boxes[i] == boxes[r]:
                    candidate = dp(l, i, k + 1) + dp(i + 1, r - 1, 0)
                    if candidate > res:
                        res = candidate
            return res

        return dp(0, n - 1, 0)