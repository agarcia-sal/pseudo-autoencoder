from typing import List, Dict, Tuple

class Solution:
    def removeBoxes(self, boxes: List[int]) -> int:
        def dp(l: int, r: int, k: int, memo: Dict[Tuple[int, int, int], int]) -> int:
            if l > r:
                return 0
            key = (l, r, k)
            if key in memo:
                return memo[key]
            # Optimize by merging boxes[r] with boxes[r-1] if they are the same
            while r > l and boxes[r] == boxes[r - 1]:
                r -= 1
                k += 1
            res = dp(l, r - 1, 0, memo) + (k + 1) ** 2
            for i in range(l, r):
                if boxes[i] == boxes[r]:
                    res = max(res, dp(l, i, k + 1, memo) + dp(i + 1, r - 1, 0, memo))
            memo[key] = res
            return res
        return dp(0, len(boxes) - 1, 0, {})