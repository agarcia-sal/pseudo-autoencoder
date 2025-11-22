import math
from typing import List

class Solution:
    def visiblePoints(self, points: List[List[int]], angle: int, location: List[int]) -> int:
        angles = []
        extra_points = 0
        loc_x, loc_y = location
        for point in points:
            x, y = point
            if x == loc_x and y == loc_y:
                extra_points += 1
                continue
            diff_y = y - loc_y
            diff_x = x - loc_x
            angle_rad = math.atan2(diff_y, diff_x)
            angle_deg = math.degrees(angle_rad)
            angles.append(angle_deg)
        angles.sort()
        extended_angles = angles + [a + 360 for a in angles]
        max_visible = 0
        left = 0
        for right in range(len(extended_angles)):
            while extended_angles[right] - extended_angles[left] > angle:
                left += 1
            current_visible = right - left + 1
            if current_visible > max_visible:
                max_visible = current_visible
        return max_visible + extra_points