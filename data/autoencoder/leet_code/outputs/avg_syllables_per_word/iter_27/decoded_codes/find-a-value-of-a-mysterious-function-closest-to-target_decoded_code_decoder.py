from typing import List

class Solution:
    def closestToTarget(self, arr: List[int], target: int) -> int:
        seen = set()
        min_diff = float('inf')
        for num in arr:
            # Update seen with bitwise AND of num and all previous seen values, plus num itself
            new_seen = {num}
            for x in seen:
                new_val = num & x
                new_seen.add(new_val)
            seen = new_seen

            for val in seen:
                diff = abs(val - target)
                if diff < min_diff:
                    min_diff = diff

        return min_diff