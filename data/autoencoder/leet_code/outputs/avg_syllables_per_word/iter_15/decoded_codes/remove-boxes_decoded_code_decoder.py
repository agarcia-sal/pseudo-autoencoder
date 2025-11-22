from typing import List, Tuple, Dict

class Solution:
    def removeBoxes(self, boxes: List[int]) -> int:
        def dp(l: int, r: int, k: int, memo: Dict[Tuple[int, int, int], int]) -> int:
            if l > r:
                return 0
            if (l, r, k) in memo:
                return memo[(l, r, k)]

            # Compress the boxes at the right with same values, increase k accordingly
            original_r = r
            original_k = k
            while r > l and boxes[r] == boxes[r - 1]:
                r -= 1
                k += 1

            res = dp(l, r - 1, 0, memo) + (k + 1) * (k + 1)
            for i in range(l, r):
                if boxes[i] == boxes[r]:
                    res = max(res, dp(l, i, k + 1, memo) + dp(i + 1, r - 1, 0, memo))
            memo[(l, r, original_k)] = res
            return res

        return dp(0, len(boxes) - 1, 0, {})