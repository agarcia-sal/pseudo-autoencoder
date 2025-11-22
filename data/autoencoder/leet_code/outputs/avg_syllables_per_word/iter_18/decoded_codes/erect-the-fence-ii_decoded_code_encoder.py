import random
import math
from typing import List, Tuple, Union


class Solution:
    def outerTrees(self, trees: List[List[int]]) -> List[Union[float, int]]:
        def dist_sq(p1: List[int], p2: List[int]) -> float:
            return (p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2

        def circumcenter(p1: List[int], p2: List[int], p3: List[int]) -> Tuple[List[float], float]:
            ax, ay = p1[0], p1[1]
            bx, by = p2[0], p2[1]
            cx, cy = p3[0], p3[1]
            d = 2 * (ax * (by - cy) + bx * (cy - ay) + cx * (ay - by))
            if d == 0:
                # Points are collinear; circumcenter is not defined normally.
                # Return a large circle or fallback (choosing average of points here)
                center = [(ax + bx + cx) / 3, (ay + by + cy) / 3]
                radius = math.sqrt(max(dist_sq(center, p) for p in (p1, p2, p3)))
                return center, radius
            ux = (
                (ax ** 2 + ay ** 2) * (by - cy)
                + (bx ** 2 + by ** 2) * (cy - ay)
                + (cx ** 2 + cy ** 2) * (ay - by)
            ) / d
            uy = (
                (ax ** 2 + ay ** 2) * (cx - bx)
                + (bx ** 2 + by ** 2) * (ax - cx)
                + (cx ** 2 + cy ** 2) * (bx - ax)
            ) / d
            center = [ux, uy]
            radius = math.sqrt((ux - ax) ** 2 + (uy - ay) ** 2)
            return center, radius

        def welzl(points: List[List[int]], boundary: List[List[int]], n: int) -> Tuple[List[float], float]:
            if n == 0 or len(boundary) == 3:
                if len(boundary) == 0:
                    return [0.0, 0.0], 0.0
                elif len(boundary) == 1:
                    return boundary[0][:2], 0.0
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

        random.shuffle(trees)
        center, radius = welzl(trees, [], len(trees))
        return [center[0], center[1], radius]