from math import atan2, degrees

def max_points_in_angle(points, location, angle):
    angles = []
    extra = 0
    for (x, y) in points:
        if (x, y) == location:
            extra += 1
            continue
        angles.append(degrees(atan2(y - location[1], x - location[0])))
    angles.sort()
    angles += [a + 360 for a in angles]
    max_vis = 0
    left = 0
    for right in range(len(angles)):
        while angles[right] - angles[left] > angle:
            left += 1
        max_vis = max(max_vis, right - left + 1)
    return max_vis + extra