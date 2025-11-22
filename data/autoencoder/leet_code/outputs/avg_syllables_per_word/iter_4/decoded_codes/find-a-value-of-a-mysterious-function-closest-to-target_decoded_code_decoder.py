class Solution:
    def closestToTarget(self, arr, target):
        seen = set()
        min_diff = float('inf')
        for num in arr:
            seen = {num & x for x in seen} | {num}
            for val in seen:
                diff = abs(val - target)
                if diff < min_diff:
                    min_diff = diff
        return min_diff