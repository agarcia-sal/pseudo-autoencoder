import math
import random
from typing import List, Tuple

class Solution:
    def outerTrees(self, trees: List[List[float]]) -> List[float]:

        def dist_sq(p1: List[float], p2: List[float]) -> float:
            return (p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2

        def circumcenter(p1: List[float], p2: List[float], p3: List[float]) -> Tuple[List[float], float]:
            ax, ay = p1
            bx, by = p2
            cx, cy = p3
            d = 2 * (ax * (by - cy) + bx * (cy - ay) + cx * (ay - by))
            if d == 0:
                # Points are collinear; circumcenter doesn't exist; 
                # fallback: return one point and a large radius
                # but per algorithm, this should not happen when 3 points define a circle
                # still we handle gracefully
                return [ax, ay], 0.0
            ax2_ay2 = ax * ax + ay * ay
            bx2_by2 = bx * bx + by * by
            cx2_cy2 = cx * cx + cy * cy

            ux = ((ax2_ay2 * (by - cy)) + (bx2_by2 * (cy - ay)) + (cx2_cy2 * (ay - by))) / d
            uy = ((ax2_ay2 * (cx - bx)) + (bx2_by2 * (ax - cx)) + (cx2_cy2 * (bx - ax))) / d
            radius = math.sqrt((ux - ax) ** 2 + (uy - ay) ** 2)
            return [ux, uy], radius

        def welzl(points: List[List[float]], boundary: List[List[float]], n: int) -> Tuple[List[float], float]:
            if n == 0 or len(boundary) == 3:
                if len(boundary) == 0:
                    return [0.0, 0.0], 0.0
                elif len(boundary) == 1:
                    return boundary[0], 0.0
                elif len(boundary) == 2:
                    mid_x = (boundary[0][0] + boundary[1][0]) / 2
                    mid_y = (boundary[0][1] + boundary[1][1]) / 2
                    radius = math.sqrt(dist_sq(boundary[0], boundary[1])) / 2
                    return [mid_x, mid_y], radius
                else:  # len(boundary) == 3
                    return circumcenter(boundary[0], boundary[1], boundary[2])

            p = points[n - 1]
            center, radius = welzl(points, boundary, n - 1)
            if dist_sq(center, p) <= radius * radius + 1e-14:
                return center, radius
            return welzl(points, boundary + [p], n - 1)

        random.shuffle(trees)
        center, radius = welzl(trees, [], len(trees))
        return [center[0], center[1], radius]