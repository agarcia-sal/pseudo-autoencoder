from typing import List, Dict, Tuple

class Solution:
    def removeBoxes(self, boxes: List[int]) -> int:
        from functools import lru_cache

        def dp(l: int, r: int, k: int, memo: Dict[Tuple[int, int, int], int]) -> int:
            if l > r:
                return 0
            if (l, r, k) in memo:
                return memo[(l, r, k)]
            # Optimize by extending the sequence of the same box at the right end
            while r > l and boxes[r] == boxes[r - 1]:
                r -= 1
                k += 1
            # Remove the boxes[r] group first
            res = dp(l, r - 1, 0, memo) + (k + 1) * (k + 1)
            # Try merging non-contiguous boxes of the same type
            for i in range(l, r):
                if boxes[i] == boxes[r]:
                    temp = dp(l, i, k + 1, memo) + dp(i + 1, r - 1, 0, memo)
                    if temp > res:
                        res = temp
            memo[(l, r, k)] = res
            return res

        return dp(0, len(boxes) - 1, 0, {})