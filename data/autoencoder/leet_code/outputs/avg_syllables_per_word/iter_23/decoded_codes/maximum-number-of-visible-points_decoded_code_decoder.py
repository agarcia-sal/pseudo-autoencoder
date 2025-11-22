import math
from typing import List

class Solution:
    def visiblePoints(self, points: List[List[int]], angle: int, location: List[int]) -> int:
        angles = []
        extra_points = 0
        loc_x, loc_y = location

        for x, y in points:
            if x == loc_x and y == loc_y:
                extra_points += 1
                continue
            diff_y = y - loc_y
            diff_x = x - loc_x
            angle_rad = math.atan2(diff_y, diff_x)
            angle_deg = math.degrees(angle_rad)
            angles.append(angle_deg)

        angles.sort()

        # Create a list with each angle + 360 to simulate a circular range
        doubled_angles = [a + 360 for a in angles]
        angles += doubled_angles

        max_visible = 0
        left = 0
        n = len(angles)
        for right in range(n):
            while angles[right] - angles[left] > angle:
                left += 1
            current_count = right - left + 1
            if current_count > max_visible:
                max_visible = current_count

        return max_visible + extra_points