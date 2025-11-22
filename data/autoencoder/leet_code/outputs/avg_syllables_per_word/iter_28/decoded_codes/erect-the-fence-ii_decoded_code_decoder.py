import math
import random
from typing import List, Tuple

class Solution:
    def outerTrees(self, trees: List[List[int]]) -> List[float]:
        def dist_sq(p1: List[int], p2: List[int]) -> float:
            dx = p1[0] - p2[0]
            dy = p1[1] - p2[1]
            return dx * dx + dy * dy

        def circumcenter(p1: List[int], p2: List[int], p3: List[int]) -> Tuple[List[float], float]:
            ax, ay = p1
            bx, by = p2
            cx, cy = p3

            d = 2 * (ax * (by - cy) + bx * (cy - ay) + cx * (ay - by))
            if d == 0:
                # Points are collinear; circumcenter is undefined.
                # Return a large circle to cover all three points
                # Alternatively return the circle with max distance between points
                dist_ab = dist_sq(p1, p2)
                dist_bc = dist_sq(p2, p3)
                dist_ca = dist_sq(p3, p1)
                max_dist = max(dist_ab, dist_bc, dist_ca)
                if max_dist == dist_ab:
                    center = [(p1[0] + p2[0]) / 2.0, (p1[1] + p2[1]) / 2.0]
                    radius = math.sqrt(dist_ab) / 2.0
                elif max_dist == dist_bc:
                    center = [(p2[0] + p3[0]) / 2.0, (p2[1] + p3[1]) / 2.0]
                    radius = math.sqrt(dist_bc) / 2.0
                else:
                    center = [(p3[0] + p1[0]) / 2.0, (p3[1] + p1[1]) / 2.0]
                    radius = math.sqrt(dist_ca) / 2.0
                return center, radius

            ax_sq = ax * ax + ay * ay
            bx_sq = bx * bx + by * by
            cx_sq = cx * cx + cy * cy

            ux_num = (ax_sq * (by - cy) + bx_sq * (cy - ay) + cx_sq * (ay - by))
            uy_num = (ax_sq * (cx - bx) + bx_sq * (ax - cx) + cx_sq * (bx - ax))

            ux = ux_num / d
            uy = uy_num / d

            diff_x = ux - ax
            diff_y = uy - ay
            radius_sq = diff_x * diff_x + diff_y * diff_y
            radius = math.sqrt(radius_sq)

            return [ux, uy], radius

        def welzl(points: List[List[int]], boundary: List[List[int]], n: int) -> Tuple[List[float], float]:
            if n == 0 or len(boundary) == 3:
                if len(boundary) == 0:
                    return [0.0, 0.0], 0.0
                if len(boundary) == 1:
                    return [float(boundary[0][0]), float(boundary[0][1])], 0.0
                if len(boundary) == 2:
                    center_x = (boundary[0][0] + boundary[1][0]) / 2.0
                    center_y = (boundary[0][1] + boundary[1][1]) / 2.0
                    center = [center_x, center_y]
                    dist_between_points = dist_sq(boundary[0], boundary[1])
                    radius = math.sqrt(dist_between_points) / 2.0
                    return center, radius
                return circumcenter(boundary[0], boundary[1], boundary[2])

            p = points[n - 1]
            center, radius = welzl(points, boundary, n - 1)
            dist_center_p = dist_sq(center, p)
            radius_sq = radius * radius
            if dist_center_p <= radius_sq + 1e-12:
                return center, radius
            return welzl(points, boundary + [p], n - 1)

        random.shuffle(trees)
        center, radius = welzl(trees, [], len(trees))
        return [center[0], center[1], radius]