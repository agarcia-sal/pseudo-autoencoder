import random
import math

class Solution:
    def outerTrees(self, trees):
        def dist_sq(p1, p2):
            return (p1[0] - p2[0])**2 + (p1[1] - p2[1])**2

        def circumcenter(p1, p2, p3):
            ax, ay = p1
            bx, by = p2
            cx, cy = p3
            d = 2 * (ax * (by - cy) + bx * (cy - ay) + cx * (ay - by))
            ux = ((ax*ax + ay*ay) * (by - cy) +
                  (bx*bx + by*by) * (cy - ay) +
                  (cx*cx + cy*cy) * (ay - by)) / d
            uy = ((ax*ax + ay*ay) * (cx - bx) +
                  (bx*bx + by*by) * (ax - cx) +
                  (cx*cx + cy*cy) * (bx - ax)) / d
            center = [ux, uy]
            radius = math.sqrt((ux - ax)**2 + (uy - ay)**2)
            return center, radius

        def welzl(points, boundary, n):
            if n == 0 or len(boundary) == 3:
                if len(boundary) == 0:
                    return [0, 0], 0
                elif len(boundary) == 1:
                    return boundary[0], 0
                elif len(boundary) == 2:
                    cx = (boundary[0][0] + boundary[1][0]) / 2
                    cy = (boundary[0][1] + boundary[1][1]) / 2
                    center = [cx, cy]
                    radius = math.sqrt(dist_sq(boundary[0], boundary[1])) / 2
                    return center, radius
                else:
                    return circumcenter(boundary[0], boundary[1], boundary[2])

            p = points[n-1]
            center, radius = welzl(points, boundary, n-1)
            if dist_sq(center, p) <= radius * radius:
                return center, radius
            return welzl(points, boundary + [p], n-1)

        points = trees[:]
        random.shuffle(points)
        center, radius = welzl(points, [], len(points))
        return [center[0], center[1], radius]