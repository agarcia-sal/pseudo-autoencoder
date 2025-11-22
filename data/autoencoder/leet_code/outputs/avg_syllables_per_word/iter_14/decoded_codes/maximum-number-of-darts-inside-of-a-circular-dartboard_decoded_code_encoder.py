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
            h_x = p1[0] + p2[0]
            h_y = p1[1] + p2[1]
            half_h_x = h_x / 2
            half_h_y = h_y / 2
            dx = p2[1] - p1[1]
            dy = p2[0] - p1[0]
            dx_scaled = dx * a / d
            dy_scaled = dy * a / d
            first_center = (half_h_x - dx_scaled, half_h_y + dy_scaled)
            second_center = (half_h_x + dx_scaled, half_h_y - dy_scaled)
            return [first_center, second_center]

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