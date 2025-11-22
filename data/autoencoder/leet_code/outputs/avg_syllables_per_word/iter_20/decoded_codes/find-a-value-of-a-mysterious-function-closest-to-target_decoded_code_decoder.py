from math import inf

class Solution:
    def closestToTarget(self, arr: list[int], target: int) -> int:
        seen = set()
        min_diff = inf
        for num in arr:
            seen = {num & x for x in seen} | {num}
            for val in seen:
                current_difference = abs(val - target)
                if current_difference < min_diff:
                    min_diff = current_difference
        return min_diff