from typing import List, Tuple, Dict

class Solution:
    def removeBoxes(self, boxes: List[int]) -> int:
        from functools import lru_cache

        n = len(boxes)

        memo: Dict[Tuple[int, int, int], int] = {}

        def dp(l: int, r: int, k: int) -> int:
            if l > r:
                return 0

            if (l, r, k) in memo:
                return memo[(l, r, k)]

            # Optimize by merging boxes[r] with boxes[r-1], boxes[r-2], ... if they are the same
            while r > l and boxes[r] == boxes[r - 1]:
                r -= 1
                k += 1

            # Remove boxes[r] together with k boxes of the same color attached
            # So we remove (k+1)^2 points plus the result of removing boxes[l:r]
            res = dp(l, r - 1, 0) + (k + 1) ** 2

            # Try to merge boxes[r] with some boxes[i] == boxes[r] in boxes[l:r]
            for i in range(l, r):
                if boxes[i] == boxes[r]:
                    # Try to remove boxes[i+1:r-1], then remove boxes[i] and boxes[r] together with k+1 attached boxes
                    res = max(res, dp(l, i, k + 1) + dp(i + 1, r - 1, 0))

            memo[(l, r, k)] = res
            return res

        return dp(0, n - 1, 0)