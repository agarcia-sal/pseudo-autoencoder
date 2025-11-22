import math
from typing import List, Optional, Tuple

class Solution:
    def numPoints(self, darts: List[List[int]], r: int) -> int:

        def distance(p1: List[int], p2: List[int]) -> float:
            dx = p1[0] - p2[0]
            dy = p1[1] - p2[1]
            return math.sqrt(dx * dx + dy * dy)

        def circle_center(p1: List[int], p2: List[int], r: int) -> Optional[List[Tuple[float, float]]]:
            d = distance(p1, p2)
            if d > 2 * r:
                return None
            r_sq = r * r
            half_d = d / 2
            half_d_sq = half_d * half_d
            a = math.sqrt(r_sq - half_d_sq)
            h_x = (p1[0] + p2[0]) / 2
            h_y = (p1[1] + p2[1]) / 2
            # To avoid division by zero when p1 == p2 (distance 0),
            # handle separately:
            if d == 0:
                # Both points are same; only one center possible at p1
                return [(h_x, h_y)]
            dx = (p2[1] - p1[1]) * a / d
            dy = (p2[0] - p1[0]) * a / d
            return [(h_x - dx, h_y + dy), (h_x + dx, h_y - dy)]

        def is_inside(circle: Tuple[float, float], point: List[int], r: int) -> bool:
            dist_to_point = math.hypot(circle[0] - point[0], circle[1] - point[1])
            return dist_to_point <= r + 1e-9  # small epsilon to handle floating point precision

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