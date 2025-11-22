from math import atan2, degrees

class Solution:
    def visiblePoints(self, points: list[list[int]], angle: int, location: list[int]) -> int:
        angles = []
        extra_points = 0
        x0, y0 = location

        for x, y in points:
            if x == x0 and y == y0:
                extra_points += 1
                continue
            angle_rad = atan2(y - y0, x - x0)
            angle_deg = degrees(angle_rad)
            angles.append(angle_deg)

        angles.sort()

        extended_angles = angles + [a + 360 for a in angles]

        max_visible = 0
        left = 0

        for right in range(len(extended_angles)):
            while extended_angles[right] - extended_angles[left] > angle:
                left += 1
            max_visible = max(max_visible, right - left + 1)

        return max_visible + extra_points