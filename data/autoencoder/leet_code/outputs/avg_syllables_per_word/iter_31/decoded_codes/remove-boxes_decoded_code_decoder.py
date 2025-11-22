from typing import List, Dict, Tuple

class Solution:
    def removeBoxes(self, boxes: List[int]) -> int:
        memo: Dict[Tuple[int, int, int], int] = {}

        def dp(l: int, r: int, k: int) -> int:
            if l > r:
                return 0
            if (l, r, k) in memo:
                return memo[(l, r, k)]

            # Optimize by merging boxes of the same color at the right edge
            while r > l and boxes[r] == boxes[r - 1]:
                r -= 1
                k += 1

            # Base case: remove the last (k+1) boxes of the same color at position r
            res = dp(l, r - 1, 0) + (k + 1) * (k + 1)

            # Try merging non-contiguous boxes of the same color to get a better score
            for i in range(l, r):
                if boxes[i] == boxes[r]:
                    possible_value = dp(l, i, k + 1) + dp(i + 1, r - 1, 0)
                    if possible_value > res:
                        res = possible_value

            memo[(l, r, k)] = res
            return res

        return dp(0, len(boxes) - 1, 0)