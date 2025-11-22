import math
from typing import List, Optional, Tuple

class Solution:
    def numPoints(self, darts: List[Tuple[int, int]], r: int) -> int:
        def distance(p1: Tuple[int, int], p2: Tuple[int, int]) -> float:
            dx = p1[0] - p2[0]
            dy = p1[1] - p2[1]
            return math.sqrt(dx*dx + dy*dy)

        def circle_center(p1: Tuple[int, int], p2: Tuple[int, int], r: int) -> Optional[List[Tuple[float, float]]]:
            d = distance(p1, p2)
            if d > 2 * r:
                return None
            half_distance = d / 2
            a = math.sqrt(r*r - half_distance*half_distance)
            midpoint_horizontal = (p1[0] + p2[0]) / 2
            midpoint_vertical = (p1[1] + p2[1]) / 2
            # Vector from p1 to p2
            dx = p2[1] - p1[1]
            dy = p2[0] - p1[0]
            # Normalize and scale to length a/d
            if d == 0:  # To avoid division by zero if points coincide
                return [(midpoint_horizontal, midpoint_vertical)]
            factor = a / d
            dx *= factor
            dy *= factor
            first_center = (midpoint_horizontal - dx, midpoint_vertical + dy)
            second_center = (midpoint_horizontal + dx, midpoint_vertical - dy)
            return [first_center, second_center]

        def is_inside(circle: Tuple[float, float], point: Tuple[int, int], r: int) -> bool:
            return distance(circle, point) <= r

        n = len(darts)
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