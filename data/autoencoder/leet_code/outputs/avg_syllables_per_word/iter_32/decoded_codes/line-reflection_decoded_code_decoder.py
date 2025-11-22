from typing import List, Tuple

class Solution:
    def isReflected(self, points: List[List[int]]) -> bool:
        unique_points = set((x, y) for x, y in points)
        if not unique_points:
            return True
        min_x = min(x for x, _ in unique_points)
        max_x = max(x for x, _ in unique_points)
        line_of_reflection = (min_x + max_x) / 2
        for x, y in unique_points:
            reflected_x = 2 * line_of_reflection - x
            # Since reflected_x can be float, but original x,y are ints,
            # convert reflected_x to int if exactly int
            if reflected_x.is_integer():
                reflected_x = int(reflected_x)
            if (reflected_x, y) not in unique_points:
                return False
        return True