import math
from typing import List, Optional, Tuple

class Solution:
    def numPoints(self, darts: List[List[int]], r: int) -> int:
        def distance(p1: List[int], p2: List[int]) -> float:
            delta_x = p1[0] - p2[0]
            delta_y = p1[1] - p2[1]
            return math.hypot(delta_x, delta_y)

        def circle_center(p1: List[int], p2: List[int], r: int) -> Optional[List[Tuple[float, float]]]:
            d = distance(p1, p2)
            if d > 2 * r:
                return None
            # Length from midpoint to circle center
            a = math.sqrt(r * r - (d / 2) ** 2)
            midpoint_x = (p1[0] + p2[0]) / 2
            midpoint_y = (p1[1] + p2[1]) / 2
            # vector perpendicular to p1p2, normalized and scaled by a
            dx = (p2[1] - p1[1]) * (a / d)
            dy = (p2[0] - p1[0]) * (a / d)
            center_one = (midpoint_x - dx, midpoint_y + dy)
            center_two = (midpoint_x + dx, midpoint_y - dy)
            return [center_one, center_two]

        def is_inside(circle: Tuple[float, float], point: List[int], r: int) -> bool:
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