from typing import List, Dict, Tuple

class Solution:
    def removeBoxes(self, boxes: List[int]) -> int:
        def dp(l: int, r: int, k: int, memo: Dict[Tuple[int, int, int], int]) -> int:
            if l > r:
                return 0
            if (l, r, k) in memo:
                return memo[(l, r, k)]

            # Merge boxes of the same color at the end (position r)
            while r > l and boxes[r] == boxes[r - 1]:
                r -= 1
                k += 1

            # Remove the last group (k+1 boxes) and solve for the remaining segment
            res = dp(l, r - 1, 0, memo) + (k + 1) * (k + 1)

            # Try merging non-contiguous boxes of the same color more optimally
            for i in range(l, r):
                if boxes[i] == boxes[r]:
                    res = max(res, dp(l, i, k + 1, memo) + dp(i + 1, r - 1, 0, memo))

            memo[(l, r, k)] = res
            return res

        return dp(0, len(boxes) - 1, 0, {})