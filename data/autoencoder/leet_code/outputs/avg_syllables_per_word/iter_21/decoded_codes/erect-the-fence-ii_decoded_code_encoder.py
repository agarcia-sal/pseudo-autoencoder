import random
from typing import List, Tuple, Union

class Solution:
    def outerTrees(self, trees: List[List[int]]) -> List[Union[List[float], float]]:
        def dist_sq(p1: List[float], p2: List[float]) -> float:
            dx = p1[0] - p2[0]
            dy = p1[1] - p2[1]
            return dx * dx + dy * dy

        def circumcenter(p1: List[float], p2: List[float], p3: List[float]) -> Tuple[List[float], float]:
            ax, ay = p1
            bx, by = p2
            cx, cy = p3

            d = 2 * (ax * (by - cy) + bx * (cy - ay) + cx * (ay - by))
            if d == 0:
                # Points are colinear; circumcenter is not well-defined.
                # Return one of the points as center and distance to max point as radius
                # To be consistent, return p1 and max dist/2
                dists = [dist_sq(p1, p2), dist_sq(p2, p3), dist_sq(p3, p1)]
                max_dist = max(dists)
                center_x = (ax + bx + cx) / 3
                center_y = (ay + by + cy) / 3
                radius = (max_dist ** 0.5) / 2
                return [center_x, center_y], radius

            a_sq = ax * ax + ay * ay
            b_sq = bx * bx + by * by
            c_sq = cx * cx + cy * cy

            ux_num = a_sq * (by - cy) + b_sq * (cy - ay) + c_sq * (ay - by)
            uy_num = a_sq * (cx - bx) + b_sq * (ax - cx) + c_sq * (bx - ax)

            ux = ux_num / d
            uy = uy_num / d

            dx = ux - ax
            dy = uy - ay
            radius = (dx * dx + dy * dy) ** 0.5

            return [ux, uy], radius

        def welzl(points: List[List[float]], boundary: List[List[float]], n: int) -> Tuple[List[float], float]:
            if n == 0 or len(boundary) == 3:
                if len(boundary) == 0:
                    return [0.0, 0.0], 0.0
                elif len(boundary) == 1:
                    return boundary[0], 0.0
                elif len(boundary) == 2:
                    p1, p2 = boundary[0], boundary[1]
                    center = [(p1[0] + p2[0]) / 2, (p1[1] + p2[1]) / 2]
                    radius = (dist_sq(p1, p2) ** 0.5) / 2
                    return center, radius
                else:
                    return circumcenter(boundary[0], boundary[1], boundary[2])

            p = points[n - 1]
            center, radius = welzl(points, boundary, n - 1)

            dist_center_p = dist_sq(center, p)
            radius_sq = radius * radius
            if dist_center_p <= radius_sq:
                return center, radius

            return welzl(points, boundary + [p], n - 1)

        random.shuffle(trees)
        center, radius = welzl(trees, [], len(trees))
        return [center[0], center[1], radius]