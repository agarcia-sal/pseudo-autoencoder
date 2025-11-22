import math
import random
from typing import List, Tuple

class Solution:
    def outerTrees(self, trees: List[List[int]]) -> List[float]:
        def dist_sq(p1: List[int], p2: List[int]) -> float:
            delta_x = p1[0] - p2[0]
            delta_y = p1[1] - p2[1]
            delta_x_squared = delta_x * delta_x
            delta_y_squared = delta_y * delta_y
            distance_squared = delta_x_squared + delta_y_squared
            return distance_squared

        def circumcenter(p1: List[int], p2: List[int], p3: List[int]) -> Tuple[List[float], float]:
            ax, ay = p1[0], p1[1]
            bx, by = p2[0], p2[1]
            cx, cy = p3[0], p3[1]

            d = 2 * (ax * (by - cy) + bx * (cy - ay) + cx * (ay - by))
            if d == 0:
                # Points are collinear or coincident; circumcenter undefined.
                # Return a large circle encompassing all points as a fallback.
                # Here we return p1 as center with very large radius.
                # In the context of Welzl's algorithm, this fallback won't be used
                # since points should be distinct and not collinear at this step.
                return [float(ax), float(ay)], float('inf')

            a_squared_sum = ax * ax + ay * ay
            b_squared_sum = bx * bx + by * by
            c_squared_sum = cx * cx + cy * cy

            numerator_ux = (a_squared_sum * (by - cy) +
                            b_squared_sum * (cy - ay) +
                            c_squared_sum * (ay - by))
            numerator_uy = (a_squared_sum * (cx - bx) +
                            b_squared_sum * (ax - cx) +
                            c_squared_sum * (bx - ax))

            ux = numerator_ux / d
            uy = numerator_uy / d

            delta_ux = ux - ax
            delta_uy = uy - ay
            radius = math.sqrt(delta_ux * delta_ux + delta_uy * delta_uy)

            return [ux, uy], radius

        def welzl(points: List[List[int]], boundary: List[List[int]], n: int) -> Tuple[List[float], float]:
            if n == 0 or len(boundary) == 3:
                if len(boundary) == 0:
                    return [0.0, 0.0], 0.0
                elif len(boundary) == 1:
                    return [float(boundary[0][0]), float(boundary[0][1])], 0.0
                elif len(boundary) == 2:
                    center_x = (boundary[0][0] + boundary[1][0]) / 2.0
                    center_y = (boundary[0][1] + boundary[1][1]) / 2.0
                    center = [center_x, center_y]
                    diameter_squared = dist_sq(boundary[0], boundary[1])
                    radius = math.sqrt(diameter_squared) / 2.0
                    return center, radius
                else:
                    # exactly 3 points
                    return circumcenter(boundary[0], boundary[1], boundary[2])

            p = points[n - 1]

            center, radius = welzl(points, boundary, n - 1)

            dist_center_p = dist_sq(center, p)

            if dist_center_p <= radius * radius + 1e-14:
                return center, radius

            return welzl(points, boundary + [p], n - 1)

        # To ensure robustness and correctness, shuffle input points
        points_copy = trees.copy()
        random.shuffle(points_copy)

        center, radius = welzl(points_copy, [], len(points_copy))

        return [center[0], center[1], radius]