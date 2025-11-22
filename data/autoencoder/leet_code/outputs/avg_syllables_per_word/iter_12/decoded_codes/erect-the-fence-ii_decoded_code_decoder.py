import random
from math import sqrt

class Solution:
    def outerTrees(self, trees):
        def dist_sq(p1, p2):
            dx = p1[0] - p2[0]
            dy = p1[1] - p2[1]
            return dx * dx + dy * dy

        def circumcenter(p1, p2, p3):
            ax, ay = p1
            bx, by = p2
            cx, cy = p3
            d = 2 * (ax * (by - cy) + bx * (cy - ay) + cx * (ay - by))
            # Colinear points might cause zero division; given problem constraints this is unlikely,
            # but to be safe, we handle that case returning a large circle.
            if d == 0:
                # Return an approximate large circle that covers all points
                # Just return a circle around p1 with radius large enough to cover p2 and p3
                max_dist = max(sqrt(dist_sq(p1, p2)), sqrt(dist_sq(p1, p3)))
                return [ax, ay], max_dist
            ux_num = (ax*ax + ay*ay)*(by - cy) + (bx*bx + by*by)*(cy - ay) + (cx*cx + cy*cy)*(ay - by)
            ux = ux_num / d
            uy_num = (ax*ax + ay*ay)*(cx - bx) + (bx*bx + by*by)*(ax - cx) + (cx*cx + cy*cy)*(bx - ax)
            uy = uy_num / d
            dx = ux - ax
            dy = uy - ay
            radius = sqrt(dx*dx + dy*dy)
            return [ux, uy], radius

        def welzl(points, boundary, n):
            if n == 0 or len(boundary) == 3:
                if len(boundary) == 0:
                    return [0.0, 0.0], 0.0
                elif len(boundary) == 1:
                    return boundary[0], 0.0
                elif len(boundary) == 2:
                    c_x = (boundary[0][0] + boundary[1][0]) / 2
                    c_y = (boundary[0][1] + boundary[1][1]) / 2
                    center = [c_x, c_y]
                    distance_sq = dist_sq(boundary[0], boundary[1])
                    radius = sqrt(distance_sq) / 2
                    return center, radius
                else:
                    return circumcenter(boundary[0], boundary[1], boundary[2])

            p = points[n - 1]
            center, radius = welzl(points, boundary, n - 1)
            if dist_sq(center, p) <= radius * radius:
                return center, radius
            return welzl(points, boundary + [p], n - 1)

        trees = trees[:]  # Make a copy to shuffle without affecting the original
        random.shuffle(trees)
        center, radius = welzl(trees, [], len(trees))
        return [center[0], center[1], radius]