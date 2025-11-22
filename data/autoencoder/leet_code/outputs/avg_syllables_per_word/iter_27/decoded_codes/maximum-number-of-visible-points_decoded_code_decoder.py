import math
from typing import List

class Solution:
    def visiblePoints(self, pointsList: List[List[int]], angleValue: int, locationList: List[int]) -> int:
        angles = []
        extra_points = 0
        loc_x, loc_y = locationList[0], locationList[1]

        for x, y in pointsList:
            if x == loc_x and y == loc_y:
                extra_points += 1
                continue
            dy = y - loc_y
            dx = x - loc_x
            angle_rad = math.atan2(dy, dx)
            angle_deg = math.degrees(angle_rad)
            # Normalize angle to [0, 360)
            if angle_deg < 0:
                angle_deg += 360
            angles.append(angle_deg)

        angles.sort()
        doubled_angles = angles + [a + 360 for a in angles]
        angles = doubled_angles

        max_visible = 0
        left = 0
        for right in range(len(angles)):
            while angles[right] - angles[left] > angleValue:
                left += 1
            max_visible = max(max_visible, right - left + 1)

        return max_visible + extra_points