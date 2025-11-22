from typing import List

class Solution:
    def closestToTarget(self, arr: List[int], target: int) -> int:
        seen = set()
        min_diff = float('inf')

        for num in arr:
            seen = {num & val for val in seen} | {num}
            for val in seen:
                min_diff = min(min_diff, abs(val - target))

        return min_diff