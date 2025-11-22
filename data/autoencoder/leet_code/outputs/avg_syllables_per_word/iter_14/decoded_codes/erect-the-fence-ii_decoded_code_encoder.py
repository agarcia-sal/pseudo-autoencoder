import random
import math
from typing import List, Tuple

class Solution:
    def outerTrees(self, trees: List[List[float]]) -> List[float]:
        def dist_sq(p1: List[float], p2: List[float]) -> float:
            dx = p1[0] - p2[0]
            dy = p1[1] - p2[1]
            return dx * dx + dy * dy

        def circumcenter(p1: List[float], p2: List[float], p3: List[float]) -> Tuple[List[float], float]:
            ax, ay = p1
            bx, by = p2
            cx, cy = p3

            part_one = ax * (by - cy)
            part_two = bx * (cy - ay)
            part_three = cx * (ay - by)
            d = 2 * (part_one + part_two + part_three)

            if d == 0:  # points are colinear, circumcenter undefined
                # Return center as midpoint of the max distance segment and radius accordingly
                dists = [(dist_sq(p1, p2), (p1, p2)),
                         (dist_sq(p2, p3), (p2, p3)),
                         (dist_sq(p3, p1), (p3, p1))]
                max_dist, (pa, pb) = max(dists, key=lambda x: x[0])
                center = [(pa[0] + pb[0]) / 2, (pa[1] + pb[1]) / 2]
                radius = math.sqrt(max_dist) / 2
                return center, radius

            ax_sq = ax * ax
            ay_sq = ay * ay
            bx_sq = bx * bx
            by_sq = by * by
            cx_sq = cx * cx
            cy_sq = cy * cy

            first_numerator = (ax_sq + ay_sq) * (by - cy)
            second_numerator = (bx_sq + by_sq) * (cy - ay)
            third_numerator = (cx_sq + cy_sq) * (ay - by)
            ux = (first_numerator + second_numerator + third_numerator) / d

            first_numerator_y = (ax_sq + ay_sq) * (cx - bx)
            second_numerator_y = (bx_sq + by_sq) * (ax - cx)
            third_numerator_y = (cx_sq + cy_sq) * (bx - ax)
            uy = (first_numerator_y + second_numerator_y + third_numerator_y) / d

            dx = ux - ax
            dy = uy - ay
            radius = math.sqrt(dx * dx + dy * dy)

            return [ux, uy], radius

        def welzl(points: List[List[float]], boundary: List[List[float]], n: int) -> Tuple[List[float], float]:
            if n == 0 or len(boundary) == 3:
                if len(boundary) == 0:
                    return [0.0, 0.0], 0.0
                elif len(boundary) == 1:
                    return boundary[0], 0.0
                elif len(boundary) == 2:
                    center = [(boundary[0][0] + boundary[1][0]) / 2,
                              (boundary[0][1] + boundary[1][1]) / 2]
                    dist = math.sqrt(dist_sq(boundary[0], boundary[1]))
                    radius = dist / 2
                    return center, radius
                else:  # len(boundary) == 3
                    return circumcenter(boundary[0], boundary[1], boundary[2])

            p = points[n - 1]

            center, radius = welzl(points, boundary, n - 1)

            dist_to_center = dist_sq(center, p)
            radius_sq = radius * radius
            if dist_to_center <= radius_sq + 1e-14:  # numeric tolerance
                return center, radius

            return welzl(points, boundary + [p], n - 1)

        random.shuffle(trees)
        center, radius = welzl(trees, [], len(trees))
        return [center[0], center[1], radius]