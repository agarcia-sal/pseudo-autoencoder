from typing import List

class Solution:
    def maximizeSweetness(self, sweetness: List[int], k: int) -> int:
        def canDivide(min_sweet: int) -> bool:
            pieces = 0
            current_sweet = 0
            for sweet in sweetness:
                current_sweet += sweet
                if current_sweet >= min_sweet:
                    pieces += 1
                    current_sweet = 0
                    if pieces > k:
                        return True
            return pieces > k

        left = min(sweetness)
        right = (sum(sweetness) // (k + 1)) + 1  # k+1 pieces means dividing sweetness into k+1 parts
        result = 0
        while left <= right:
            mid = (left + right) // 2
            if canDivide(mid):
                result = mid
                left = mid + 1
            else:
                right = mid - 1
        return result