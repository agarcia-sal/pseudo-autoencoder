import math
import random
from typing import List, Tuple

class Solution:
    def outerTrees(self, trees: List[List[int]]) -> List[float]:
        # Calculate squared distance between two points
        def dist_sq(p1: List[float], p2: List[float]) -> float:
            dx = p1[0] - p2[0]
            dy = p1[1] - p2[1]
            return dx * dx + dy * dy

        # Calculate the circumcenter and radius of the circle through points p1, p2, p3
        def circumcenter(p1: List[float], p2: List[float], p3: List[float]) -> Tuple[List[float], float]:
            ax, ay = p1
            bx, by = p2
            cx, cy = p3

            part_one = bx * (by - cy)
            part_two = cx * (ay - by)
            part_three = ax * (by - cy)
            d = 2 * (ax * (by - cy) + part_one + part_two)
            if abs(d) < 1e-15:
                # Points are collinear or very close, circumcenter undefined
                # Return a large circle or a circle from two points, fallback
                # We'll handle collinear points as circle with max distance of two points
                # Find max dist between pairs in p1,p2,p3 and form circle accordingly
                pts = [p1, p2, p3]
                max_dist = 0
                center = [0.0, 0.0]
                radius = 0.0
                for i in range(3):
                    for j in range(i + 1,3):
                        dist = dist_sq(pts[i], pts[j])
                        if dist > max_dist:
                            max_dist = dist
                            center = [(pts[i][0] + pts[j][0]) / 2, (pts[i][1] + pts[j][1]) / 2]
                            radius = math.sqrt(max_dist) / 2
                return center, radius

            squared_ax = ax * ax
            squared_ay = ay * ay
            squared_bx = bx * bx
            squared_by = by * by
            squared_cx = cx * cx
            squared_cy = cy * cy

            numerator_ux = ((squared_ax + squared_ay) * (by - cy) +
                            (squared_bx + squared_by) * (cy - ay) +
                            (squared_cx + squared_cy) * (ay - by))
            numerator_uy = ((squared_ax + squared_ay) * (cx - bx) +
                            (squared_bx + squared_by) * (ax - cx) +
                            (squared_cx + squared_cy) * (bx - ax))

            ux = numerator_ux / d
            uy = numerator_uy / d

            dx = ux - ax
            dy = uy - ay
            radius_sq = dx * dx + dy * dy
            radius = math.sqrt(radius_sq)

            return [ux, uy], radius

        # Welzl's algorithm to find minimum enclosing circle recursively
        def welzl(points: List[List[float]], boundary: List[List[float]], n: int) -> Tuple[List[float], float]:
            if n == 0 or len(boundary) == 3:
                if len(boundary) == 0:
                    return [0.0, 0.0], 0.0
                elif len(boundary) == 1:
                    return boundary[0], 0.0
                elif len(boundary) == 2:
                    p1, p2 = boundary[0], boundary[1]
                    center = [(p1[0] + p2[0]) / 2, (p1[1] + p2[1]) / 2]
                    dist = dist_sq(p1, p2)
                    radius = math.sqrt(dist) / 2
                    return center, radius
                else:  # 3 points
                    return circumcenter(boundary[0], boundary[1], boundary[2])

            p = points[n - 1]
            center, radius = welzl(points, boundary, n - 1)

            dx = p[0] - center[0]
            dy = p[1] - center[1]
            dist_sq_p_center = dx*dx + dy*dy
            if dist_sq_p_center <= radius * radius + 1e-15:
                return center, radius

            new_boundary = boundary + [p]
            return welzl(points, new_boundary, n - 1)

        # Defensive copy to avoid modifying input and shuffle
        points = [list(map(float, p)) for p in trees]
        random.shuffle(points)

        center, radius = welzl(points, [], len(points))
        return [center[0], center[1], radius]