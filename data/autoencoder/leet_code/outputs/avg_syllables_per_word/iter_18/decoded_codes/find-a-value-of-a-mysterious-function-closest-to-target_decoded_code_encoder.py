class Solution:
    def closestToTarget(self, arr: list[int], target: int) -> int:
        seen = set()
        min_diff = float('inf')
        for num in arr:
            temp = {num & x for x in seen}
            temp.add(num)
            seen = temp
            for val in seen:
                diff = abs(val - target)
                if diff < min_diff:
                    min_diff = diff
        return min_diff