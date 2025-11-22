import math
from typing import List, Optional, Tuple

class Solution:
    def numPoints(self, darts: List[List[int]], r: int) -> int:
        def distance(p1: Tuple[float, float], p2: Tuple[float, float]) -> float:
            dx = p1[0] - p2[0]
            dy = p1[1] - p2[1]
            return math.sqrt(dx * dx + dy * dy)

        def circle_center(p1: Tuple[float, float], p2: Tuple[float, float], r: float) -> Optional[List[Tuple[float, float]]]:
            d = distance(p1, p2)
            if d > 2 * r:
                return None
            half_distance = d / 2
            # To avoid floating errors causing sqrt of negative
            # clamp argument to zero minimum
            a_sq = r * r - half_distance * half_distance
            if a_sq < 0:
                a_sq = 0.0
            a = math.sqrt(a_sq)

            midpoint_horizontal = (p1[0] + p2[0]) / 2
            midpoint_vertical = (p1[1] + p2[1]) / 2

            # perpendicular vector components scaled by a/d
            dx = (p2[1] - p1[1]) * a / d
            dy = (p2[0] - p1[0]) * a / d

            first_center = (midpoint_horizontal - dx, midpoint_vertical + dy)
            second_center = (midpoint_horizontal + dx, midpoint_vertical - dy)
            return [first_center, second_center]

        def is_inside(circle: Tuple[float, float], point: Tuple[float, float], r: float) -> bool:
            return distance(circle, point) <= r + 1e-10  # small epsilon for floating tolerance

        n = len(darts)
        if n == 1:
            return 1

        max_count = 1

        points = [(float(x), float(y)) for x, y in darts]

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