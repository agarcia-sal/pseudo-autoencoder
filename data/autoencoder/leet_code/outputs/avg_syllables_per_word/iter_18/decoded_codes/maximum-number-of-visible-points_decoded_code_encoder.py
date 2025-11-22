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
            dx = x - loc_x
            dy = y - loc_y
            angle_in_radians = math.atan2(dy, dx)
            angle_in_degrees = math.degrees(angle_in_radians)
            angles.append(angle_in_degrees)

        angles.sort()
        extended_angles = angles + [a + 360 for a in angles]
        angles = extended_angles

        max_visible = 0
        left = 0
        for right in range(len(angles)):
            while angles[right] - angles[left] > angle:
                left += 1
            current_window_size = right - left + 1
            if current_window_size > max_visible:
                max_visible = current_window_size

        return max_visible + extra_points