import math
from typing import List

class Solution:
    def visiblePoints(self, points: List[List[int]], angle: int, location: List[int]) -> int:
        angles = []
        extra_points = 0
        loc_x, loc_y = location[0], location[1]

        for point in points:
            x, y = point[0], point[1]
            if x == loc_x and y == loc_y:
                extra_points += 1
                continue
            angle_deg = self.CalculateAngleDegrees(y - loc_y, x - loc_x)
            angles.append(angle_deg)

        angles = self.SortList(angles)

        duplicated_angles = [a + 360 for a in angles]
        angles += duplicated_angles

        max_visible = 0
        left = 0
        n = len(angles)
        for right in range(n):
            while angles[right] - angles[left] > angle:
                left += 1
            current_visible = right - left + 1
            if current_visible > max_visible:
                max_visible = current_visible

        return max_visible + extra_points

    def CalculateAngleDegrees(self, delta_y: float, delta_x: float) -> float:
        # Use atan2 to get correct angle with sign and quadrant, convert radians to degrees.
        return math.degrees(math.atan2(delta_y, delta_x))

    def SortList(self, list_to_sort: List[float]) -> List[float]:
        return sorted(list_to_sort)