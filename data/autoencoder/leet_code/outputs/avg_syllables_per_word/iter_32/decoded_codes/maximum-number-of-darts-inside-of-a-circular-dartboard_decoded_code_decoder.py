import math
from typing import List, Optional, Tuple

class Solution:
    def numPoints(self, darts: List[List[int]], r: int) -> int:
        def distance(p1: List[int], p2: List[int]) -> float:
            dx = p1[0] - p2[0]
            dy = p1[1] - p2[1]
            return math.hypot(dx, dy)

        def circle_center(p1: List[int], p2: List[int], r: int) -> Optional[List[List[float]]]:
            d = distance(p1, p2)
            if d > 2 * r:
                return None
            # half-distance along the line segment
            mid_x = (p1[0] + p2[0]) / 2
            mid_y = (p1[1] + p2[1]) / 2
            # distance from midpoint to the circle centers
            # inside_square_root = r^2 - (d/2)^2
            inside_sqrt = r * r - (d / 2) * (d / 2)
            # If inside_sqrt is very close to zero due to floating point errors, clamp to zero to avoid math domain errors
            if inside_sqrt < 0:
                inside_sqrt = 0.0
            a = math.sqrt(inside_sqrt)

            # The vector from p1 to p2
            dx = (p2[0] - p1[0]) / d if d != 0 else 0
            dy = (p2[1] - p1[1]) / d if d != 0 else 0

            # Perpendicular vectors to the line segment p1p2
            # Two possible circle centers
            center1 = [mid_x - dy * a, mid_y + dx * a]
            center2 = [mid_x + dy * a, mid_y - dx * a]

            return [center1, center2]

        def is_inside(center: List[float], point: List[int], r: int) -> bool:
            return distance(center, point) <= r + 1e-9  # Add a small epsilon for floating point tolerance

        n = len(darts)
        if n == 1:
            return 1

        max_count = 1  # at least one dart can be covered by a circle

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