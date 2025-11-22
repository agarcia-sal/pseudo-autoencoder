import math
from typing import List, Optional

class Solution:
    def numPoints(self, darts: List[List[int]], r: int) -> int:
        def distance(p1: List[int], p2: List[int]) -> float:
            dx = p1[0] - p2[0]
            dy = p1[1] - p2[1]
            return math.sqrt(dx * dx + dy * dy)

        def circle_center(p1: List[int], p2: List[int], r: int) -> Optional[List[List[float]]]:
            d = distance(p1, p2)
            if d > 2 * r:
                return None
            a = math.sqrt(r * r - (d / 2) * (d / 2))
            midpoint_x = (p1[0] + p2[0]) / 2
            midpoint_y = (p1[1] + p2[1]) / 2
            dx = (p2[1] - p1[1]) * a / d
            dy = (p2[0] - p1[0]) * a / d
            first_center = [midpoint_x - dx, midpoint_y + dy]
            second_center = [midpoint_x + dx, midpoint_y - dy]
            return [first_center, second_center]

        def is_inside(circle: List[float], point: List[int], r: int) -> bool:
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