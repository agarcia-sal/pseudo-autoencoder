import math

def dist(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def circle_centers(p1, p2, r):
    d = dist(p1, p2)
    if d > 2 * r:
        return None
    a = math.sqrt(r**2 - (d/2)**2)
    h_x = (p1[0] + p2[0]) / 2
    h_y = (p1[1] + p2[1]) / 2
    dx = (p2[1] - p1[1]) * (a / d)
    dy = (p2[0] - p1[0]) * (a / d)
    return [(h_x - dx, h_y + dy), (h_x + dx, h_y - dy)]

def inside(c, p, r):
    return dist(c, p) <= r

def numPoints(darts, r):
    n = len(darts)
    if n == 1:
        return 1
    max_c = 1
    for i in range(n):
        for j in range(i + 1, n):
            centers = circle_centers(darts[i], darts[j], r)
            if centers is not None:
                for c in centers:
                    count = sum(inside(c, d, r) for d in darts)
                    max_c = max(max_c, count)
    return max_c