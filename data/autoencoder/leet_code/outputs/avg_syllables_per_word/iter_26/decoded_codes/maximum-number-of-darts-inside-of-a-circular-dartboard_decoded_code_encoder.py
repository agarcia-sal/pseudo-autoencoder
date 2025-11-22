import math
from typing import List, Tuple, Optional

class Solution:
    def numPoints(self, darts: List[List[int]], r: int) -> int:
        def distance(p1: Tuple[int, int], p2: Tuple[int, int]) -> float:
            return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

        def circle_center(p1: Tuple[int, int], p2: Tuple[int, int], r: int) -> Optional[List[Tuple[float, float]]]:
            d = distance(p1, p2)
            if d > 2 * r:
                return None
            a = math.sqrt(r * r - (d / 2) ** 2)
            h = [(p1[0] + p2[0]) / 2, (p1[1] + p2[1]) / 2]
            dx = (p2[1] - p1[1]) * a / d
            dy = (p2[0] - p1[0]) * a / d
            return [(h[0] - dx, h[1] + dy), (h[0] + dx, h[1] - dy)]

        def is_inside(center: Tuple[float, float], point: Tuple[int, int], r: int) -> bool:
            return distance(center, point) <= r

        n = len(darts)
        if n == 1:
            return 1

        max_count = 1

        # Convert darts to tuple format for consistent hashability and usage
        points = [tuple(d) for d in darts]

        for i in range(n):
            for j in range(i + 1, n):
                centers = circle_center(points[i], points[j], r)
                if centers is not None:
                    for center in centers:
                        count = 0
                        for dart in points:
                            if is_inside(center, dart, r):
                                count += 1
                        if count > max_count:
                            max_count = count

        return max_count