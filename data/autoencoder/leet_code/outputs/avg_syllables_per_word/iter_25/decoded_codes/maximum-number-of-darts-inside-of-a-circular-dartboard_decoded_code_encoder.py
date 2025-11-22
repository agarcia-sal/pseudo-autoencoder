import math
from typing import List, Optional, Tuple


class Solution:
    def numPoints(self, darts: List[Tuple[int, int]], r: int) -> int:
        def distance(p1: Tuple[int, int], p2: Tuple[int, int]) -> float:
            dx = p1[0] - p2[0]
            dy = p1[1] - p2[1]
            return math.sqrt(dx * dx + dy * dy)

        def circle_center(p1: Tuple[int, int], p2: Tuple[int, int], r: int) -> Optional[List[Tuple[float, float]]]:
            d = distance(p1, p2)
            if d > 2 * r:
                return None
            a = math.sqrt(r * r - (d / 2) * (d / 2))
            h_horizontal = (p1[0] + p2[0]) / 2
            h_vertical = (p1[1] + p2[1]) / 2
            dx = (p2[1] - p1[1]) * a / d
            dy = (p2[0] - p1[0]) * a / d
            first_center = (h_horizontal - dx, h_vertical + dy)
            second_center = (h_horizontal + dx, h_vertical - dy)
            return [first_center, second_center]

        def is_inside(circle: Tuple[float, float], point: Tuple[int, int], r: int) -> bool:
            return distance(circle, point) <= r

        n = len(darts)
        if n == 1:
            return 1

        max_count = 1

        # Consider each point as a center to cover at least one dart
        for i in range(n):
            count_point_center = 0
            for dart in darts:
                if distance(darts[i], dart) <= r:
                    count_point_center += 1
            if count_point_center > max_count:
                max_count = count_point_center

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