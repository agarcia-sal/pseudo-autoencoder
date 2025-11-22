import math
from typing import List, Optional, Tuple

class Solution:
    def numPoints(self, darts: List[List[int]], r: int) -> int:
        def distance(p1: Tuple[float, float], p2: Tuple[float, float]) -> float:
            dx = p1[0] - p2[0]
            dy = p1[1] - p2[1]
            return math.hypot(dx, dy)

        def circle_center(p1: Tuple[float, float], p2: Tuple[float, float], r: float) -> Optional[List[Tuple[float, float]]]:
            d = distance(p1, p2)
            if d > 2 * r:
                return None
            # Half distance between points
            half_d = d / 2.0
            # Distance from midpoint to circle centers along perpendicular
            a = math.sqrt(r*r - half_d*half_d)
            # Midpoint coordinates
            midpoint_x = (p1[0] + p2[0]) / 2.0
            midpoint_y = (p1[1] + p2[1]) / 2.0

            # dx, dy are the components of a perpendicular vector scaled by a/d
            # perpendicular vector to (p2 - p1) is (-(y2 - y1), x2 - x1)
            dx = (p2[1] - p1[1]) * (a / d)
            dy = (p1[0] - p2[0]) * (a / d)

            center1 = (midpoint_x - dx, midpoint_y - dy)
            center2 = (midpoint_x + dx, midpoint_y + dy)
            return [center1, center2]

        def is_inside(circle: Tuple[float, float], point: Tuple[float, float], r: float) -> bool:
            return distance(circle, point) <= r + 1e-10

        n = len(darts)
        if n == 1:
            return 1

        max_count = 1
        points = [tuple(dart) for dart in darts]

        for i in range(n):
            for j in range(i + 1, n):
                centers = circle_center(points[i], points[j], r)
                if centers is not None:
                    for center in centers:
                        count = 0
                        for dart in points:
                            if is_inside(center, dart, r):
                                count += 1
                        if count > max_count:
                            max_count = count

        return max_count