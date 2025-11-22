from typing import List, Tuple, Set

class Solution:
    def isReflected(self, points: List[List[int]]) -> bool:
        unique_points: Set[Tuple[int, int]] = set((x, y) for x, y in points)
        min_x = min(x for x, _ in unique_points)
        max_x = max(x for x, _ in unique_points)
        line_of_reflection = (min_x + max_x) / 2
        for x, y in unique_points:
            reflected_x = 2 * line_of_reflection - x
            if (reflected_x, y) not in unique_points:
                return False
        return True