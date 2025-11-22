class Solution:
    def closestToTarget(self, arr, target):
        seen = set()
        min_diff = float('inf')
        for num in arr:
            temporary_set = {num}
            for x in seen:
                temporary_set.add(num & x)
            seen = temporary_set
            for val in seen:
                diff = abs(val - target)
                if diff < min_diff:
                    min_diff = diff
        return min_diff