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

        # Calculate the circumcenter and radius of the circle through three points
        def circumcenter(p1: List[float], p2: List[float], p3: List[float]) -> Tuple[List[float], float]:
            ax, ay = p1
            bx, by = p2
            cx, cy = p3

            d = 2 * (ax * (by - cy) + bx * (cy - ay) + cx * (ay - by))
            if abs(d) < 1e-15:
                # Points are collinear or extremely close: circumcenter ill-defined
                # We can fallback to returning a circle that covers all three points
                # For fallback, pick the circle with center at midpoint of the max distance pair
                points = [p1, p2, p3]
                max_dist = 0
                max_pair = (p1, p1)
                for i in range(3):
                    for j in range(i + 1, 3):
                        ds = dist_sq(points[i], points[j])
                        if ds > max_dist:
                            max_dist = ds
                            max_pair = (points[i], points[j])
                center = [(max_pair[0][0] + max_pair[1][0]) / 2, (max_pair[0][1] + max_pair[1][1]) / 2]
                radius = math.sqrt(max_dist) / 2
                return center, radius

            ux = (
                ((ax * ax + ay * ay) * (by - cy)) +
                ((bx * bx + by * by) * (cy - ay)) +
                ((cx * cx + cy * cy) * (ay - by))
            ) / d
            uy = (
                ((ax * ax + ay * ay) * (cx - bx)) +
                ((bx * bx + by * by) * (ax - cx)) +
                ((cx * cx + cy * cy) * (bx - ax))
            ) / d
            center = [ux, uy]
            radius = math.sqrt((ux - ax)**2 + (uy - ay)**2)
            return center, radius

        # Welzl's algorithm to find the minimal enclosing circle for a set of points
        def welzl(points: List[List[float]], boundary: List[List[float]], n: int) -> Tuple[List[float], float]:
            if n == 0 or len(boundary) == 3:
                if len(boundary) == 0:
                    return [0.0, 0.0], 0.0
                elif len(boundary) == 1:
                    return boundary[0], 0.0
                elif len(boundary) == 2:
                    p1, p2 = boundary[0], boundary[1]
                    center = [(p1[0] + p2[0]) / 2.0, (p1[1] + p2[1]) / 2.0]
                    radius = math.sqrt(dist_sq(p1, p2)) / 2.0
                    return center, radius
                else:
                    return circumcenter(boundary[0], boundary[1], boundary[2])

            p = points[n - 1]
            center, radius = welzl(points, boundary, n - 1)
            if dist_sq(center, p) <= radius * radius + 1e-14:
                return center, radius

            # Point p is outside the current circle; add to boundary and recurse
            return welzl(points, boundary + [p], n - 1)

        # Convert all input points to floats for precision and consistency
        points = [[float(x), float(y)] for x, y in trees]

        random.shuffle(points)
        center, radius = welzl(points, [], len(points))
        return [center[0], center[1], radius]