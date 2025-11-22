from math import atan2, degrees

class Solution:
    def visiblePoints(self, points, angle, location):
        angles = []
        extra_points = 0
        x0, y0 = location

        for x, y in points:
            if x == x0 and y == y0:
                extra_points += 1
                continue
            angle_deg = degrees(atan2(y - y0, x - x0))
            angles.append(angle_deg)

        angles.sort()
        angles += [a + 360 for a in angles]

        max_visible = 0
        left = 0
        n = len(angles) // 2

        for right in range(len(angles)):
            while angles[right] - angles[left] > angle:
                left += 1
            window_size = right - left + 1
            if window_size > max_visible:
                max_visible = window_size

        return max_visible + extra_points