import random
import math
from typing import List, Tuple

class Solution:
    def outerTrees(self, trees: List[List[int]]) -> List[float]:

        def dist_sq(p1: List[int], p2: List[int]) -> float:
            return (p1[0] - p2[0])**2 + (p1[1] - p2[1])**2

        def circumcenter(p1: List[int], p2: List[int], p3: List[int]) -> Tuple[List[float], float]:
            ax, ay = p1[0], p1[1]
            bx, by = p2[0], p2[1]
            cx, cy = p3[0], p3[1]

            d = 2 * (ax*(by - cy) + bx*(cy - ay) + cx*(ay - by))
            if d == 0:
                # Points are collinear, circumcenter undefined; return a large radius circle containing all points
                # Or fallback: return centroid and max dist as radius
                cx_mean = (ax + bx + cx) / 3
                cy_mean = (ay + by + cy) / 3
                radius = math.sqrt(max(dist_sq([cx_mean, cy_mean], p) for p in [p1, p2, p3]))
                return [cx_mean, cy_mean], radius

            ux = ((ax*ax + ay*ay)*(by - cy) + (bx*bx + by*by)*(cy - ay) + (cx*cx + cy*cy)*(ay - by)) / d
            uy = ((ax*ax + ay*ay)*(cx - bx) + (bx*bx + by*by)*(ax - cx) + (cx*cx + cy*cy)*(bx - ax)) / d
            radius = math.sqrt((ux - ax)**2 + (uy - ay)**2)
            return [ux, uy], radius

        def welzl(points: List[List[int]], boundary: List[List[int]], n: int) -> Tuple[List[float], float]:
            if n == 0 or len(boundary) == 3:
                if len(boundary) == 0:
                    return [0.0, 0.0], 0.0
                elif len(boundary) == 1:
                    return list(boundary[0]), 0.0
                elif len(boundary) == 2:
                    center = [(boundary[0][0] + boundary[1][0]) / 2.0,
                              (boundary[0][1] + boundary[1][1]) / 2.0]
                    radius = math.sqrt(dist_sq(boundary[0], boundary[1])) / 2.0
                    return center, radius
                else:
                    return circumcenter(boundary[0], boundary[1], boundary[2])

            p = points[n-1]
            center, radius = welzl(points, boundary, n - 1)
            if dist_sq(center, p) <= radius**2 + 1e-14:
                return center, radius

            return welzl(points, boundary + [p], n - 1)

        random.shuffle(trees)
        center, radius = welzl(trees, [], len(trees))
        return [center[0], center[1], radius]