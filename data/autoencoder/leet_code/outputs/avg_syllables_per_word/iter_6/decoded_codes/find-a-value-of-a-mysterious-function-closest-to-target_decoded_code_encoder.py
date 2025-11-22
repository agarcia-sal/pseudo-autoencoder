class Solution:
    def closestToTarget(self, arr, target):
        seen = set()
        min_diff = float('inf')

        for num in arr:
            new_seen = {num}
            for x in seen:
                new_seen.add(num & x)
            seen = new_seen
            min_diff = min(min_diff, min(abs(val - target) for val in seen))

        return min_diff