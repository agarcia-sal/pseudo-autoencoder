import math
from typing import List

class Solution:
    def visiblePoints(self, points: List[List[int]], angle: int, location: List[int]) -> int:
        angles = []
        same_location_count = 0
        loc_x, loc_y = location

        for x, y in points:
            if x == loc_x and y == loc_y:
                same_location_count += 1
                continue
            dx = x - loc_x
            dy = y - loc_y
            angle_rad = math.atan2(dy, dx)  # returns angle in radians [-pi, pi]
            angle_deg = math.degrees(angle_rad)
            if angle_deg < 0:
                angle_deg += 360  # normalize to [0, 360)
            angles.append(angle_deg)

        angles.sort()
        # Duplicate the array with each element + 360 to handle circular wrap-around
        extended_angles = angles + [a + 360 for a in angles]

        max_visible = 0
        left = 0

        for right in range(len(extended_angles)):
            while extended_angles[right] - extended_angles[left] > angle:
                left += 1
            current_window_size = right - left + 1
            if current_window_size > max_visible:
                max_visible = current_window_size

        return max_visible + same_location_count