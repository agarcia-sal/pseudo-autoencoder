import math
from typing import List, Tuple, Optional


class Solution:
    def numPoints(self, darts: List[Tuple[float, float]], r: float) -> int:
        def distance(p1: Tuple[float, float], p2: Tuple[float, float]) -> float:
            dx = p1[0] - p2[0]
            dy = p1[1] - p2[1]
            return math.sqrt(dx * dx + dy * dy)

        def circle_center(
            p1: Tuple[float, float], p2: Tuple[float, float], r: float
        ) -> Optional[List[Tuple[float, float]]]:
            d = distance(p1, p2)
            if d > 2 * r:
                return None
            a = math.sqrt(r * r - (d / 2) * (d / 2))
            h_horizontal = (p1[0] + p2[0]) / 2
            h_vertical = (p1[1] + p2[1]) / 2
            # To get perpendicular offsets, swap dx and dy and negate one
            dx = (p2[1] - p1[1]) * a / d if d != 0 else 0.0
            dy = (p2[0] - p1[0]) * a / d if d != 0 else 0.0
            first_center = (h_horizontal - dx, h_vertical + dy)
            second_center = (h_horizontal + dx, h_vertical - dy)
            return [first_center, second_center]

        def is_inside(circle: Tuple[float, float], point: Tuple[float, float], r: float) -> bool:
            return distance(circle, point) <= r + 1e-12

        n = len(darts)
        if n == 0:
            return 0
        if n == 1:
            return 1

        max_count = 1

        for i in range(n):
            for j in range(i + 1, n):
                centers = circle_center(darts[i], darts[j], r)
                if centers is not None:
                    for center in centers:
                        count = 0
                        for dart in darts:
                            if is_inside(center, dart, r):
                                count += 1
                        if count > max_count:
                            max_count = count

        return max_count