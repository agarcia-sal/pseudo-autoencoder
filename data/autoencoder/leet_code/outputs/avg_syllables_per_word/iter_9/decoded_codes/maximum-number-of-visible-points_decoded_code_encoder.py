import math

class Solution:
    def visiblePoints(self, points, angle, location):
        angles = []
        extra_points = 0
        x0, y0 = location

        for x, y in points:
            if x == x0 and y == y0:
                extra_points += 1
                continue
            angle_deg = math.degrees(math.atan2(y - y0, x - x0))
            angles.append(angle_deg)

        angles.sort()
        angles += [a + 360 for a in angles]

        max_visible = left = 0
        for right in range(len(angles)):
            while angles[right] - angles[left] > angle:
                left += 1
            max_visible = max(max_visible, right - left + 1)

        return max_visible + extra_points