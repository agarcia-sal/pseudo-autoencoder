from typing import List

class Solution:
    def closestToTarget(self, arr: List[int], target: int) -> int:
        seen = set()
        min_diff = float('inf')

        for num in arr:
            temp = {num}
            for val in seen:
                temp.add(val & num)
            seen = temp

            for val in seen:
                diff = abs(val - target)
                if diff < min_diff:
                    min_diff = diff

        return min_diff