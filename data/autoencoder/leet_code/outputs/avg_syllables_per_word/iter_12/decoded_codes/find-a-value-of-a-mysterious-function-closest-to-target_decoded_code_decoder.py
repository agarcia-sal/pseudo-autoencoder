class Solution:
    def closestToTarget(self, arr, target):
        seen = set()
        min_diff = float('inf')
        for num in arr:
            # Compute bitwise AND between current num and all elements in seen, plus num itself
            seen = {num} | {num & x for x in seen}
            # Update min_diff with the smallest absolute difference found
            min_diff = min(min_diff, min(abs(val - target) for val in seen))
        return min_diff