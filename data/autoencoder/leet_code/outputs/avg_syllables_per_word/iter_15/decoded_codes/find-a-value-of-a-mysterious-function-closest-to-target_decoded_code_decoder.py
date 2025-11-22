from typing import List

class Solution:
    def closestToTarget(self, arr: List[int], target: int) -> int:
        seen = set()
        min_diff = float('inf')
        for num in arr:
            temp = {num & x for x in seen}
            temp.add(num)
            seen = temp
            for val in seen:
                current_difference = abs(val - target)
                if current_difference < min_diff:
                    min_diff = current_difference
        return min_diff