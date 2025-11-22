from math import atan2, degrees

class Solution:
    def visiblePoints(self, points, angle, location):
        angles = []
        extra_points = 0

        x_loc, y_loc = location

        for point in points:
            x, y = point
            if x == x_loc and y == y_loc:
                extra_points += 1
                continue
            angle_rad = atan2(y - y_loc, x - x_loc)
            angle_deg = degrees(angle_rad)
            angles.append(angle_deg)

        angles.sort()

        extended_angles = angles + [a + 360 for a in angles]
        angles = extended_angles

        max_visible = 0
        left = 0

        for right in range(len(angles)):
            while angles[right] - angles[left] > angle:
                left += 1
            max_visible = max(max_visible, right - left + 1)

        return max_visible + extra_points