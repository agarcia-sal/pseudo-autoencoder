import math
from typing import List, Tuple, Optional

class Solution:
    def numPoints(self, darts: List[List[int]], r: int) -> int:
        def distance(p1: Tuple[float, float], p2: Tuple[float, float]) -> float:
            return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

        def circle_center(p1: Tuple[float, float], p2: Tuple[float, float], r: float) -> Optional[List[Tuple[float, float]]]:
            d = distance(p1, p2)
            if d > 2 * r:
                return None
            # midpoint between p1 and p2
            h = ((p1[0] + p2[0]) / 2, (p1[1] + p2[1]) / 2)
            # half the distance from midpoint to circle center along the perpendicular bisector
            a = math.sqrt(r ** 2 - (d / 2) ** 2)
            # perpendicular offsets
            dx = (p2[1] - p1[1]) * (a / d)
            dy = (p2[0] - p1[0]) * (a / d)
            return [(h[0] - dx, h[1] + dy), (h[0] + dx, h[1] - dy)]

        def is_inside(circle: Tuple[float, float], point: Tuple[float, float], r: float) -> bool:
            return distance(circle, point) <= r

        n = len(darts)
        if n == 1:
            return 1

        max_count = 1
        points = [tuple(d) for d in darts]  # Convert input lists to tuples for clarity

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