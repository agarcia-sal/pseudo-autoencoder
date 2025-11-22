class Solution:
    def closestToTarget(self, arr, target):
        seen = set()
        min_diff = float('inf')

        for num in arr:
            new_seen = {num & x for x in seen}
            new_seen.add(num)
            seen = new_seen

            for val in seen:
                diff = abs(val - target)
                if diff < min_diff:
                    min_diff = diff
        return min_diff