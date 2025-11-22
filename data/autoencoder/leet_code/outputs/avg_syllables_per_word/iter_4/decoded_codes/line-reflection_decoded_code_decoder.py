from typing import List

class Solution:
    def isReflected(self, points: List[List[int]]) -> bool:
        unique_points = set()
        for p in points:
            # Convert null-like values to None if needed, but coordinates are integers here.
            # Just ensure tuples are valid.
            if p is None or len(p) != 2:
                continue
            x, y = p
            unique_points.add((x, y))

        if not unique_points:
            return True

        min_x = min(x for x, _ in unique_points)
        max_x = max(x for x, _ in unique_points)
        line_of_reflection = (min_x + max_x) / 2

        for x, y in unique_points:
            reflected_x = 2 * line_of_reflection - x
            # reflected_x might be float due to division, but all original x are int
            # Need to check existence possibly with float or int? Since original points are int
            # reflected_x can be half-integers. So check as float.
            if (reflected_x, y) not in unique_points:
                return False
        return True