from typing import List

class Solution:
    def isReflected(self, points: List[List[int]]) -> bool:
        unique_points = {tuple(point) for point in points}
        if not unique_points:
            return True
        min_x = min(p[0] for p in unique_points)
        max_x = max(p[0] for p in unique_points)
        line_of_reflection = (min_x + max_x) / 2
        for x, y in unique_points:
            reflected_x = 2 * line_of_reflection - x
            if (reflected_x, y) not in unique_points:
                return False
        return True