import math
from typing import List, Optional, Tuple


class Solution:
    def numPoints(self, darts: List[List[int]], r: int) -> int:
        def distance(p1: List[int], p2: List[int]) -> float:
            dx = p1[0] - p2[0]
            dy = p1[1] - p2[1]
            return math.sqrt(dx * dx + dy * dy)

        def circle_center(p1: List[int], p2: List[int], r: int) -> Optional[List[List[float]]]:
            dist = distance(p1, p2)
            if dist > 2 * r:
                return None
            # Halfway between p1 and p2
            mid_x = (p1[0] + p2[0]) / 2.0
            mid_y = (p1[1] + p2[1]) / 2.0
            # Distance from midpoint to circle centers along the perpendicular bisector
            h = math.sqrt(r * r - (dist / 2) * (dist / 2))
            # Direction vector from p1 to p2
            dx = p2[0] - p1[0]
            dy = p2[1] - p1[1]
            # Normalize perpendicular vector (dy, -dx)
            # Multiply by h / dist
            offset_x = dy * (h / dist)
            offset_y = -dx * (h / dist)
            center1 = [mid_x - offset_x, mid_y - offset_y]
            center2 = [mid_x + offset_x, mid_y + offset_y]
            return [center1, center2]

        def is_inside(circle: List[float], point: List[int], r: int) -> bool:
            return distance(circle, point) <= r + 1e-9  # Add small epsilon to handle floating errors

        n = len(darts)
        if n == 1:
            return 1

        max_count = 1  # At least one dart can always be covered

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