class Solution:
    def closestToTarget(self, arr, target):
        seen = set()
        min_diff = float('inf')

        for num in arr:
            seen = {num} | {num & val for val in seen}
            min_diff = min(min_diff, min(abs(val - target) for val in seen))

        return min_diff