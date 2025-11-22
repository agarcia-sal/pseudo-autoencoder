from typing import List

class Solution:
    def closestToTarget(self, arr: List[int], target: int) -> int:
        seen = set()
        min_diff = float('inf')
        for num in arr:
            new_seen = set()
            for x in seen:
                new_seen.add(num & x)
            new_seen.add(num)
            seen = new_seen
            for val in seen:
                diff = abs(val - target)
                if diff < min_diff:
                    min_diff = diff
        return min_diff