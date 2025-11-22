import math

class Solution:
    def visiblePoints(self, points, angle, location):
        angles = []
        extra_points = 0

        for x, y in points:
            if x == location[0] and y == location[1]:
                extra_points += 1
                continue
            angle_rad = math.atan2(y - location[1], x - location[0])
            angle_deg = math.degrees(angle_rad)
            angles.append(angle_deg)

        angles.sort()
        angles += [a + 360 for a in angles]

        max_visible = 0
        left = 0

        for right in range(len(angles)):
            while angles[right] - angles[left] > angle:
                left += 1
            max_visible = max(max_visible, right - left + 1)

        return max_visible + extra_points