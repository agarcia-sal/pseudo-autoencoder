import random
import math
from typing import List, Tuple, Union

class Solution:
    def outerTrees(self, trees: List[List[int]]) -> List[float]:
        def dist_sq(p1: List[float], p2: List[float]) -> float:
            dx = p1[0] - p2[0]
            dy = p1[1] - p2[1]
            return dx * dx + dy * dy

        def circumcenter(p1: List[float], p2: List[float], p3: List[float]) -> Tuple[List[float], float]:
            ax, ay = p1[0], p1[1]
            bx, by = p2[0], p2[1]
            cx, cy = p3[0], p3[1]
            d = 2 * (ax * (by - cy) + bx * (cy - ay) + cx * (ay - by))
            if d == 0:
                # Points are collinear; return some default values
                # Center arbitrary, radius large enough to cover points
                # Use midpoint of the longest segment as center, radius half of that segment
                d12 = dist_sq(p1, p2)
                d23 = dist_sq(p2, p3)
                d31 = dist_sq(p3, p1)
                max_d = max(d12, d23, d31)
                if max_d == d12:
                    center = [(p1[0] + p2[0]) / 2, (p1[1] + p2[1]) / 2]
                    radius = math.sqrt(d12) / 2
                elif max_d == d23:
                    center = [(p2[0] + p3[0]) / 2, (p2[1] + p3[1]) / 2]
                    radius = math.sqrt(d23) / 2
                else:
                    center = [(p3[0] + p1[0]) / 2, (p3[1] + p1[1]) / 2]
                    radius = math.sqrt(d31) / 2
                return center, radius

            ux = (((ax * ax + ay * ay) * (by - cy)) +
                  ((bx * bx + by * by) * (cy - ay)) +
                  ((cx * cx + cy * cy) * (ay - by))) / d
            uy = (((ax * ax + ay * ay) * (cx - bx)) +
                  ((bx * bx + by * by) * (ax - cx)) +
                  ((cx * cx + cy * cy) * (bx - ax))) / d
            center = [ux, uy]
            radius = math.sqrt((ux - ax) ** 2 + (uy - ay) ** 2)
            return center, radius

        def welzl(points: List[List[float]], boundary: List[List[float]], n: int) -> Tuple[List[float], float]:
            if n == 0 or len(boundary) == 3:
                if len(boundary) == 0:
                    return [0.0, 0.0], 0.0
                elif len(boundary) == 1:
                    return boundary[0][:], 0.0
                elif len(boundary) == 2:
                    c = [(boundary[0][0] + boundary[1][0]) / 2, (boundary[0][1] + boundary[1][1]) / 2]
                    r = math.sqrt(dist_sq(boundary[0], boundary[1])) / 2
                    return c, r
                else:
                    return circumcenter(boundary[0], boundary[1], boundary[2])

            p = points[n - 1]
            center, radius = welzl(points, boundary, n - 1)
            if dist_sq(center, p) <= radius * radius + 1e-14:
                return center, radius
            return welzl(points, boundary + [p], n - 1)

        points = [[float(x), float(y)] for x, y in trees]
        random.shuffle(points)
        center, radius = welzl(points, [], len(points))
        return [center[0], center[1], radius]