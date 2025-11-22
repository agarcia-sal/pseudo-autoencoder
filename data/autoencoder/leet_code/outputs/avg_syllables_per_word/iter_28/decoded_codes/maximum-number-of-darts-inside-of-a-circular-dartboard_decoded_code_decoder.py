import math
from typing import List, Optional, Tuple


class Solution:
    def numPoints(self, darts: List[List[int]], r: int) -> int:
        def distance(p1: Tuple[float, float], p2: Tuple[float, float]) -> float:
            delta_x = p1[0] - p2[0]
            delta_y = p1[1] - p2[1]
            return math.sqrt(delta_x * delta_x + delta_y * delta_y)

        def circle_center(p1: Tuple[float, float], p2: Tuple[float, float], r: float) -> Optional[List[Tuple[float, float]]]:
            dist = distance(p1, p2)
            if dist > 2 * r:
                return None
            a = math.sqrt(r * r - (dist / 2) * (dist / 2))
            midpoint_x = (p1[0] + p2[0]) / 2
            midpoint_y = (p1[1] + p2[1]) / 2
            dx = (p2[1] - p1[1]) * a / dist if dist != 0 else 0.0
            dy = (p2[0] - p1[0]) * a / dist if dist != 0 else 0.0
            first_center = (midpoint_x - dx, midpoint_y + dy)
            second_center = (midpoint_x + dx, midpoint_y - dy)
            return [first_center, second_center]

        def is_inside(circle: Tuple[float, float], point: Tuple[float, float], r: float) -> bool:
            return distance(circle, point) <= r + 1e-9  # Add epsilon to handle floating point precision

        n = len(darts)
        if n == 1:
            return 1

        max_count = 1
        points = [tuple(d) for d in darts]

        for i in range(n):
            for j in range(i + 1, n):
                centers = circle_center(points[i], points[j], r)
                if centers is not None:
                    for c in centers:
                        count = 0
                        for dart in points:
                            if is_inside(c, dart, r):
                                count += 1
                        if count > max_count:
                            max_count = count

        return max_count