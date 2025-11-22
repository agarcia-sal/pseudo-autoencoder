import math
import random
from typing import List, Tuple

class Solution:
    def outerTrees(self, trees: List[List[int]]) -> List[float]:
        def dist_sq(p1: List[float], p2: List[float]) -> float:
            return (p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2

        def circumcenter(p1: List[float], p2: List[float], p3: List[float]) -> Tuple[List[float], float]:
            ax, ay = p1[0], p1[1]
            bx, by = p2[0], p2[1]
            cx, cy = p3[0], p3[1]

            d = 2 * (ax * (by - cy) + bx * (cy - ay) + cx * (ay - by))
            if d == 0:
                # Points are collinear or very close, circumcenter is undefined
                # Return some fallback: center as midpoint of the longest segment, radius as half that segment
                dists = [
                    (dist_sq(p1, p2), (p1, p2)),
                    (dist_sq(p2, p3), (p2, p3)),
                    (dist_sq(p3, p1), (p3, p1))
                ]
                max_dist, (pa, pb) = max(dists, key=lambda x: x[0])
                center = [(pa[0] + pb[0]) / 2, (pa[1] + pb[1]) / 2]
                radius = math.sqrt(max_dist) / 2
                return center, radius

            ux = (
                ((ax * ax + ay * ay) * (by - cy) +
                 (bx * bx + by * by) * (cy - ay) +
                 (cx * cx + cy * cy) * (ay - by))
                / d
            )
            uy = (
                ((ax * ax + ay * ay) * (cx - bx) +
                 (bx * bx + by * by) * (ax - cx) +
                 (cx * cx + cy * cy) * (bx - ax))
                / d
            )
            center = [ux, uy]
            radius = math.sqrt((ux - ax)**2 + (uy - ay)**2)
            return center, radius

        def welzl(points: List[List[float]], boundary: List[List[float]], n: int) -> Tuple[List[float], float]:
            if n == 0 or len(boundary) == 3:
                if len(boundary) == 0:
                    return [0.0, 0.0], 0.0
                elif len(boundary) == 1:
                    return boundary[0], 0.0
                elif len(boundary) == 2:
                    mid = [
                        (boundary[0][0] + boundary[1][0]) / 2,
                        (boundary[0][1] + boundary[1][1]) / 2,
                    ]
                    radius = math.sqrt(dist_sq(boundary[0], boundary[1])) / 2
                    return mid, radius
                else:
                    return circumcenter(boundary[0], boundary[1], boundary[2])

            p = points[n - 1]
            center, radius = welzl(points, boundary, n - 1)

            # Check if p is inside circle
            if dist_sq(center, p) <= radius * radius + 1e-14:
                return center, radius

            # p is outside circle, add to boundary and recurse
            return welzl(points, boundary + [p], n - 1)

        random.shuffle(trees)
        center, radius = welzl(trees, [], len(trees))
        return [center[0], center[1], radius]