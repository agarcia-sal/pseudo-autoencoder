import math
from bisect import bisect_right

class Solution:
    def visiblePoints(self, points, angle, location):
        angles = []
        extra_points = 0
        x0, y0 = location

        for x, y in points:
            if x == x0 and y == y0:
                extra_points += 1
                continue
            ang = math.degrees(math.atan2(y - y0, x - x0))
            angles.append(ang)

        angles.sort()
        angles += [ang + 360 for ang in angles]

        max_visible = 0
        left = 0
        n = len(angles)
        for right in range(n):
            while angles[right] - angles[left] > angle:
                left += 1
            max_visible = max(max_visible, right - left + 1)

        return max_visible + extra_points