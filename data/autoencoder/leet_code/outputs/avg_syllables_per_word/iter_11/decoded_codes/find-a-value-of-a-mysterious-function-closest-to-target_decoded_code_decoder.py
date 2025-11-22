class Solution:
    def closestToTarget(self, arr, target):
        seen = set()
        min_diff = float('inf')
        for num in arr:
            updated_set = set()
            for x in seen:
                updated_set.add(num & x)
            seen = updated_set | {num}
            for val in seen:
                current_diff = abs(val - target)
                if current_diff < min_diff:
                    min_diff = current_diff
        return min_diff