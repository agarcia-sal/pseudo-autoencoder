import random
import math
from collections import namedtuple

Point = namedtuple('Point', ['x', 'y'])

def dist_sq(p1, p2):
    return (p1.x - p2.x)**2 + (p1.y - p2.y)**2

def circumcenter(a, b, c):
    d = 2 * (a.x * (b.y - c.y) + b.x * (c.y - a.y) + c.x * (a.y - b.y))
    ux = ((a.x**2 + a.y**2)*(b.y - c.y) + (b.x**2 + b.y**2)*(c.y - a.y) + (c.x**2 + c.y**2)*(a.y - b.y)) / d
    uy = ((a.x**2 + a.y**2)*(c.x - b.x) + (b.x**2 + b.y**2)*(a.x - c.x) + (c.x**2 + c.y**2)*(b.x - a.x)) / d
    r = math.sqrt((ux - a.x)**2 + (uy - a.y)**2)
    return Point(ux, uy), r

def welzl(pts, boundary, n):
    if n == 0 or len(boundary) == 3:
        if len(boundary) == 0:
            return Point(0, 0), 0
        if len(boundary) == 1:
            return boundary[0], 0
        if len(boundary) == 2:
            mid = Point((boundary[0].x + boundary[1].x) / 2,
                        (boundary[0].y + boundary[1].y) / 2)
            r = math.sqrt(dist_sq(boundary[0], boundary[1])) / 2
            return mid, r
        # len(boundary) == 3
        return circumcenter(boundary[0], boundary[1], boundary[2])

    p = pts[n-1]
    c, r = welzl(pts, boundary, n-1)
    if dist_sq(c, p) <= r*r:
        return c, r
    return welzl(pts, boundary + [p], n-1)

def minimum_enclosing_circle(points):
    pts = points[:]
    random.shuffle(pts)
    center, radius = welzl(pts, [], len(pts))
    return [center.x, center.y, radius]