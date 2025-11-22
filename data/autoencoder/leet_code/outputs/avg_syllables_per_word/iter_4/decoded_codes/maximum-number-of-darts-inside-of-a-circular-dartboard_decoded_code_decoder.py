import math
from typing import List, Optional, Tuple

class Solution:
    def numPoints(self, darts: List[List[Optional[float]]], r: float) -> int:
        def distance(p1: List[float], p2: List[float]) -> float:
            dx = p1[0] - p2[0]
            dy = p1[1] - p2[1]
            return math.hypot(dx, dy)

        def circle_center(p1: List[float], p2: List[float], r: float) -> Optional[List[Tuple[float, float]]]:
            d = distance(p1, p2)
            if d > 2 * r:
                return None
            a = math.sqrt(r * r - (d / 2) ** 2)
            h = [(p1[0] + p2[0]) / 2, (p1[1] + p2[1]) / 2]
            dx = (p2[1] - p1[1]) * a / d
            dy = (p2[0] - p1[0]) * a / d
            return [(h[0] - dx, h[1] + dy), (h[0] + dx, h[1] - dy)]

        def is_inside(circle: Tuple[float, float], point: List[float], r: float) -> bool:
            return distance(list(circle), point) <= r

        n = len(darts)
        if n == 1:
            return 1

        max_count = 1

        for i in range(n - 1):
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