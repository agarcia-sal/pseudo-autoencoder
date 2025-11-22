import math
import random
from typing import List, Tuple


class Solution:
    def outerTrees(self, trees: List[List[int]]) -> List[float]:
        def dist_sq(p1: List[float], p2: List[float]) -> float:
            return (p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2

        def circumcenter(p1: List[float], p2: List[float], p3: List[float]) -> Tuple[List[float], float]:
            ax, ay = p1
            bx, by = p2
            cx, cy = p3

            d = 2 * (ax * (by - cy) + bx * (cy - ay) + cx * (ay - by))
            # If points are colinear, circumcenter is undefined; handle safely:
            if d == 0:
                # Colinear points; fallback: return midpoint of farthest points and radius covering all 3
                # Find max distance pair of points
                pairs = [(p1, p2), (p2, p3), (p1, p3)]
                max_pair = max(pairs, key=lambda pair: dist_sq(pair[0], pair[1]))
                center = [(max_pair[0][0] + max_pair[1][0]) / 2,
                          (max_pair[0][1] + max_pair[1][1]) / 2]
                radius = math.sqrt(dist_sq(center, max_pair[0]))
                return center, radius

            ux = ((ax * ax + ay * ay) * (by - cy) +
                  (bx * bx + by * by) * (cy - ay) +
                  (cx * cx + cy * cy) * (ay - by)) / d

            uy = ((ax * ax + ay * ay) * (cx - bx) +
                  (bx * bx + by * by) * (ax - cx) +
                  (cx * cx + cy * cy) * (bx - ax)) / d

            center = [ux, uy]
            radius = math.sqrt((ux - ax) ** 2 + (uy - ay) ** 2)
            return center, radius

        def welzl(points: List[List[float]], boundary: List[List[float]], n: int) -> Tuple[List[float], float]:
            if n == 0 or len(boundary) == 3:
                if not boundary:
                    return [0.0, 0.0], 0.0
                if len(boundary) == 1:
                    return boundary[0], 0.0
                if len(boundary) == 2:
                    center = [(boundary[0][0] + boundary[1][0]) / 2,
                              (boundary[0][1] + boundary[1][1]) / 2]
                    radius = math.sqrt(dist_sq(boundary[0], boundary[1])) / 2
                    return center, radius
                return circumcenter(boundary[0], boundary[1], boundary[2])

            p = points[n - 1]
            center, radius = welzl(points, boundary, n - 1)

            if dist_sq(center, p) <= radius * radius:
                return center, radius

            return welzl(points, boundary + [p], n - 1)

        pts = [list(map(float, p)) for p in trees]
        random.shuffle(pts)
        center, radius = welzl(pts, [], len(pts))
        return [center[0], center[1], radius]