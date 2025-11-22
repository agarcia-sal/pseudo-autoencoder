import random
import math
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
            # To avoid division by zero, although with distinct points this should not happen
            if d == 0:
                # Points are collinear; circumcenter is undefined.
                # Return a large radius to cover all points or handle gracefully.
                # But given welzl's algorithm usage, this may not occur.
                return [0, 0], float('inf')

            ax2_ay2 = ax**2 + ay**2
            bx2_by2 = bx**2 + by**2
            cx2_cy2 = cx**2 + cy**2

            ux = ((ax2_ay2) * (by - cy) + (bx2_by2) * (cy - ay) + (cx2_cy2) * (ay - by)) / d
            uy = ((ax2_ay2) * (cx - bx) + (bx2_by2) * (ax - cx) + (cx2_cy2) * (bx - ax)) / d
            center = [ux, uy]
            radius = math.sqrt((ux - ax)**2 + (uy - ay)**2)
            return center, radius

        def welzl(points: List[List[float]], boundary: List[List[float]], n: int) -> Tuple[List[float], float]:
            if n == 0 or len(boundary) == 3:
                if len(boundary) == 0:
                    return [0, 0], 0.0
                elif len(boundary) == 1:
                    return boundary[0], 0.0
                elif len(boundary) == 2:
                    p1, p2 = boundary[0], boundary[1]
                    center = [(p1[0] + p2[0]) / 2, (p1[1] + p2[1]) / 2]
                    radius = math.sqrt(dist_sq(p1, p2)) / 2
                    return center, radius
                else:
                    return circumcenter(boundary[0], boundary[1], boundary[2])

            p = points[n - 1]
            center, radius = welzl(points, boundary, n - 1)
            if dist_sq(center, p) <= radius * radius + 1e-14:
                return center, radius
            return welzl(points, boundary + [p], n - 1)

        # Shuffle input points to improve performance of Welzl’s algorithm
        points = [list(map(float, pt)) for pt in trees]  # ensure floats for precision
        random.shuffle(points)
        center, radius = welzl(points, [], len(points))
        return [center[0], center[1], radius]