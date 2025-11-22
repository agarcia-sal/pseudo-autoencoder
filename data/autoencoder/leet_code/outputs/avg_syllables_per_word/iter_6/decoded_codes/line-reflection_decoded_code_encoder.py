class Solution:
    def isReflected(self, points):
        unique_points = set(map(tuple, points))
        min_x = min(x for x, y in unique_points)
        max_x = max(x for x, y in unique_points)
        line_of_reflection = (min_x + max_x) / 2

        for x, y in unique_points:
            reflected_x = 2 * line_of_reflection - x
            if (reflected_x, y) not in unique_points:
                return False
        return True