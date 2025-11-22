import math
from typing import List, Tuple, Optional

class Solution:
    def numPoints(self, darts: List[Tuple[int, int]], r: int) -> int:
        def distance(p1: Tuple[int, int], p2: Tuple[int, int]) -> float:
            difference_x = p1[0] - p2[0]
            difference_y = p1[1] - p2[1]
            square_x = difference_x * difference_x
            square_y = difference_y * difference_y
            sum_squares = square_x + square_y
            result = math.sqrt(sum_squares)
            return result

        def circle_center(p1: Tuple[int, int], p2: Tuple[int, int], r: int) -> Optional[List[Tuple[float, float]]]:
            d = distance(p1, p2)
            if d > 2 * r:
                return None
            half_d = d / 2
            a = math.sqrt(r * r - half_d * half_d)
            h_x = (p1[0] + p2[0]) / 2
            h_y = (p1[1] + p2[1]) / 2
            dx = (p2[1] - p1[1]) * a / d
            dy = (p2[0] - p1[0]) * a / d
            center1 = (h_x - dx, h_y + dy)
            center2 = (h_x + dx, h_y - dy)
            return [center1, center2]

        def is_inside(circle: Tuple[float, float], point: Tuple[int, int], r: int) -> bool:
            dist = distance(circle, point)
            return dist <= r

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