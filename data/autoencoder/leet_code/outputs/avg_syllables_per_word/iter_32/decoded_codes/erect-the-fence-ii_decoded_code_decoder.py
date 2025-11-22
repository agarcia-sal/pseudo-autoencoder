import random
import math
from typing import List, Tuple, Union

class Solution:
    def outerTrees(self, trees: List[List[int]]) -> List[Union[List[float], float]]:
        def dist_sq(p1: List[int], p2: List[int]) -> float:
            dx = p1[0] - p2[0]
            dy = p1[1] - p2[1]
            return dx * dx + dy * dy

        def circumcenter(p1: List[int], p2: List[int], p3: List[int]) -> Tuple[List[float], float]:
            ax, ay = p1[0], p1[1]
            bx, by = p2[0], p2[1]
            cx, cy = p3[0], p3[1]

            d = 2 * (ax * (by - cy) + bx * (cy - ay) + cx * (ay - by))
            if d == 0:
                # Degenerate case: points are collinear or nearly so
                # As a fallback, return the minimal circle covering these points:
                # By returning the circle with largest distance between pairs, center at midpoint,
                # but since circumcenter not defined, return large enough circle
                # However, per given pseudocode, just return circumcenter normally (d can't be zero).
                # Here we handle gracefully by returning circumcenter at midpoint of max segment.
                # But since pseudocode does not specify, we fallback:
                # Return big radius and arbitrary center to cover points.
                # To preserve strict logic, let's raise ValueError to show invalid usage.
                # But to preserve flow, return a circle that covers all points: midpoint of farthest pair
                # and radius distance/2.

                pairs = [(p1,p2), (p2,p3), (p3,p1)]
                max_d = -1
                max_pair = (p1, p2)
                for a, b in pairs:
                    dist = dist_sq(a, b)
                    if dist > max_d:
                        max_d = dist
                        max_pair = (a, b)
                center = [(max_pair[0][0] + max_pair[1][0]) / 2.0, (max_pair[0][1] + max_pair[1][1]) / 2.0]
                radius = math.sqrt(max_d) / 2.0
                return center, radius

            ux = (((ax*ax + ay*ay) * (by - cy)
                 + (bx*bx + by*by) * (cy - ay)
                 + (cx*cx + cy*cy) * (ay - by)) / d)
            uy = (((ax*ax + ay*ay) * (cx - bx)
                 + (bx*bx + by*by) * (ax - cx)
                 + (cx*cx + cy*cy) * (bx - ax)) / d)
            center_point = [ux, uy]

            radius_value = math.sqrt((ux - ax)**2 + (uy - ay)**2)
            return center_point, radius_value

        def welzl(points: List[List[int]], boundary: List[List[int]], n: int) -> Tuple[List[float], float]:
            if n == 0 or len(boundary) == 3:
                if len(boundary) == 0:
                    return [0.0, 0.0], 0.0
                elif len(boundary) == 1:
                    return [float(boundary[0][0]), float(boundary[0][1])], 0.0
                elif len(boundary) == 2:
                    center_point = [
                        (boundary[0][0] + boundary[1][0]) / 2.0,
                        (boundary[0][1] + boundary[1][1]) / 2.0,
                    ]
                    radius_value = math.sqrt(dist_sq(boundary[0], boundary[1])) / 2.0
                    return center_point, radius_value
                else:
                    return circumcenter(boundary[0], boundary[1], boundary[2])

            p = points[n - 1]
            center, radius = welzl(points, boundary, n - 1)
            if dist_sq(center, p) <= radius * radius + 1e-14:  # Add small epsilon for floating error
                return center, radius

            return welzl(points, boundary + [p], n - 1)

        random.shuffle(trees)
        center_and_radius = welzl(trees, [], len(trees))
        center, radius = center_and_radius
        return [center, radius]