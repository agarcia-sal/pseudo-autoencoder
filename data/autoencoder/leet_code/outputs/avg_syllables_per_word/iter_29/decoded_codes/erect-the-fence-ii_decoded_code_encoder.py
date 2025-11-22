import random
import math
from typing import List, Tuple

class Solution:
    def outerTrees(self, trees: List[List[int]]) -> List[float]:
        def dist_sq(p1: List[int], p2: List[int]) -> float:
            dx = p1[0] - p2[0]
            dy = p1[1] - p2[1]
            return dx * dx + dy * dy

        def circumcenter(p1: List[int], p2: List[int], p3: List[int]) -> Tuple[List[float], float]:
            ax, ay = p1[0], p1[1]
            bx, by = p2[0], p2[1]
            cx, cy = p3[0], p3[1]

            term1 = ax * (by - cy)
            term2 = bx * (cy - ay)
            term3 = cx * (ay - by)
            d = 2 * (term1 + term2 + term3)
            if d == 0:
                # Points are colinear; circumcenter undefined; treat specially:
                # Return largest circle through the three points as a fallback (max of pairwise midpoints)
                # But problem context probably excludes this or tolerate returning a large radius circle.
                # We will return a circle that covers all points by taking max distance between points and the midpoint.
                pts = [p1, p2, p3]
                max_dist = 0
                center = [0.0, 0.0]
                for i in range(3):
                    for j in range(i+1,3):
                        mid_x = (pts[i][0] + pts[j][0]) / 2
                        mid_y = (pts[i][1] + pts[j][1]) / 2
                        dist = math.sqrt(dist_sq(pts[i], pts[j])) / 2
                        if dist > max_dist:
                            max_dist = dist
                            center = [mid_x, mid_y]
                return center, max_dist

            squared_ax = ax * ax + ay * ay
            squared_bx = bx * bx + by * by
            squared_cx = cx * cx + cy * cy

            ux_numerator = (squared_ax * (by - cy) +
                            squared_bx * (cy - ay) +
                            squared_cx * (ay - by))
            ux = ux_numerator / d

            uy_numerator = (squared_ax * (cx - bx) +
                            squared_bx * (ax - cx) +
                            squared_cx * (bx - ax))
            uy = uy_numerator / d

            dx = ux - ax
            dy = uy - ay
            radius = math.sqrt(dx * dx + dy * dy)
            return [ux, uy], radius

        def welzl(points: List[List[int]], boundary: List[List[int]], n: int) -> Tuple[List[float], float]:
            if n == 0 or len(boundary) == 3:
                if len(boundary) == 0:
                    return [0.0, 0.0], 0.0
                elif len(boundary) == 1:
                    return [float(boundary[0][0]), float(boundary[0][1])], 0.0
                elif len(boundary) == 2:
                    p1, p2 = boundary[0], boundary[1]
                    center_x = (p1[0] + p2[0]) / 2.0
                    center_y = (p1[1] + p2[1]) / 2.0
                    radius = math.sqrt(dist_sq(p1, p2)) / 2.0
                    return [center_x, center_y], radius
                else:
                    return circumcenter(boundary[0], boundary[1], boundary[2])

            p = points[n - 1]
            center, radius = welzl(points, boundary, n - 1)
            dist_center_p = dist_sq(center, p)
            if dist_center_p <= radius * radius:
                return center, radius
            new_boundary = boundary + [p]
            return welzl(points, new_boundary, n - 1)

        random.shuffle(trees)
        center, radius = welzl(trees, [], len(trees))
        return [center[0], center[1], radius]