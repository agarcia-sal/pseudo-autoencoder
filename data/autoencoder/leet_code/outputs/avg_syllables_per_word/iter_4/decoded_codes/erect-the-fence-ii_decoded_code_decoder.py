import math
import random
from typing import List, Tuple

class Solution:
    def outerTrees(self, trees: List[List[int]]) -> List[float]:
        def dist_sq(p1: List[int], p2: List[int]) -> float:
            return (p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2

        def circumcenter(p1: List[int], p2: List[int], p3: List[int]) -> Tuple[List[float], float]:
            ax, ay = p1
            bx, by = p2
            cx, cy = p3

            d = 2 * (ax * (by - cy) + bx * (cy - ay) + cx * (ay - by))
            # To avoid division by zero or nearly zero (collinear points),
            # add a small epsilon check.
            if abs(d) < 1e-15:
                # Fallback: one of the edges' midpoint with radius as half-length.
                # This case can be handled differently but here we fallback robustly:
                # Return a circle that covers all three points (the max distance).
                pts = [p1, p2, p3]
                max_dist = 0
                center = [0.0, 0.0]
                for i in range(3):
                    for j in range(i + 1, 3):
                        mid = [(pts[i][0] + pts[j][0]) / 2, (pts[i][1] + pts[j][1]) / 2]
                        r = math.sqrt(dist_sq(pts[i], pts[j]) / 4)
                        # Check if all points lie inside circle defined by mid and r
                        if all(dist_sq(mid, pt) <= r * r + 1e-15 for pt in pts):
                            if r > max_dist:
                                max_dist = r
                                center = mid
                if max_dist == 0:
                    # All three points are the same
                    return [float(ax), float(ay)], 0.0
                return center, max_dist

            ax_sq = ax * ax
            ay_sq = ay * ay
            bx_sq = bx * bx
            by_sq = by * by
            cx_sq = cx * cx
            cy_sq = cy * cy

            ux = ((ax_sq + ay_sq) * (by - cy) + (bx_sq + by_sq) * (cy - ay) + (cx_sq + cy_sq) * (ay - by)) / d
            uy = ((ax_sq + ay_sq) * (cx - bx) + (bx_sq + by_sq) * (ax - cx) + (cx_sq + cy_sq) * (bx - ax)) / d

            radius = math.sqrt((ux - ax) ** 2 + (uy - ay) ** 2)
            return [ux, uy], radius

        def welzl(points: List[List[int]], boundary: List[List[int]], n: int) -> Tuple[List[float], float]:
            if n == 0 or len(boundary) == 3:
                if len(boundary) == 0:
                    return [0.0, 0.0], 0.0
                elif len(boundary) == 1:
                    return [float(boundary[0][0]), float(boundary[0][1])], 0.0
                elif len(boundary) == 2:
                    mid = [(boundary[0][0] + boundary[1][0]) / 2.0, (boundary[0][1] + boundary[1][1]) / 2.0]
                    radius = math.sqrt(dist_sq(boundary[0], boundary[1])) / 2.0
                    return mid, radius
                else:
                    return circumcenter(boundary[0], boundary[1], boundary[2])

            p = points[n - 1]
            center, radius = welzl(points, boundary, n - 1)

            if dist_sq(center, p) <= radius * radius + 1e-15:
                return center, radius

            return welzl(points, boundary + [p], n - 1)

        # Defensive copy to avoid side effects; convert lists possibly containing None to int if any
        pts = [[int(x[0]), int(x[1])] for x in trees if x is not None and x[0] is not None and x[1] is not None]

        random.shuffle(pts)
        center, radius = welzl(pts, [], len(pts))
        return [center[0], center[1], radius]