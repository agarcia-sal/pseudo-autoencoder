import math
from typing import List

class Solution:
    def visiblePoints(self, points: List[List[int]], angle: int, location: List[int]) -> int:
        angles = []
        extra_points = 0

        loc_x, loc_y = location[0], location[1]

        for x, y in points:
            if x == loc_x and y == loc_y:
                extra_points += 1
                continue
            angle_rad = math.atan2(y - loc_y, x - loc_x)
            angle_deg = math.degrees(angle_rad)
            angles.append(angle_deg)

        angles.sort()
        n = len(angles)
        # Extend the angles with each angle + 360 to simulate circular wrap-around
        angles.extend(a + 360 for a in angles)

        max_visible = 0
        left = 0

        for right in range(len(angles)):
            while angles[right] - angles[left] > angle:
                left += 1
            max_visible = max(max_visible, right - left + 1)

        return max_visible + extra_points