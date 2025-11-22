from math import inf

class Solution:
    def closestToTarget(self, arr, target):
        seen = set()
        min_diff = inf
        for num in arr:
            new_seen = {num & x for x in seen}
            seen = new_seen | {num}
            for val in seen:
                diff = abs(val - target)
                if diff < min_diff:
                    min_diff = diff
        return min_diff