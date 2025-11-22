import random
from math import sqrt

class Solution:
    def outerTrees(self, trees):
        def dist_sq(p1, p2):
            dx = p1[0] - p2[0]
            dy = p1[1] - p2[1]
            return dx * dx + dy * dy

        def circumcenter(p1, p2, p3):
            ax, ay = p1
            bx, by = p2
            cx, cy = p3

            term_one = ax * (by - cy)
            term_two = bx * (cy - ay)
            term_three = cx * (ay - by)
            d = 2 * (term_one + term_two + term_three)

            sum_squares_ax_ay = ax * ax + ay * ay
            sum_squares_bx_by = bx * bx + by * by
            sum_squares_cx_cy = cx * cx + cy * cy

            ux_numerator = (
                sum_squares_ax_ay * (by - cy)
                + sum_squares_bx_by * (cy - ay)
                + sum_squares_cx_cy * (ay - by)
            )
            ux = ux_numerator / d

            uy_numerator = (
                sum_squares_ax_ay * (cx - bx)
                + sum_squares_bx_by * (ax - cx)
                + sum_squares_cx_cy * (bx - ax)
            )
            uy = uy_numerator / d

            radius_sq_component_one = ux - ax
            radius_sq_component_two = uy - ay
            radius_sq = radius_sq_component_one * radius_sq_component_one + radius_sq_component_two * radius_sq_component_two
            radius = sqrt(radius_sq)

            return [ux, uy], radius

        def welzl(points, boundary, n):
            if n == 0 or len(boundary) == 3:
                if len(boundary) == 0:
                    return [0.0, 0.0], 0.0
                elif len(boundary) == 1:
                    return boundary[0], 0.0
                elif len(boundary) == 2:
                    midpoint = [
                        (boundary[0][0] + boundary[1][0]) / 2.0,
                        (boundary[0][1] + boundary[1][1]) / 2.0,
                    ]
                    dist = dist_sq(boundary[0], boundary[1])
                    radius = sqrt(dist) / 2.0
                    return midpoint, radius
                else:
                    return circumcenter(boundary[0], boundary[1], boundary[2])
            p = points[n - 1]
            center, radius = welzl(points, boundary, n - 1)
            if dist_sq(center, p) <= radius * radius:
                return center, radius
            return welzl(points, boundary + [p], n - 1)

        random.shuffle(trees)
        center, radius = welzl(trees, [], len(trees))
        return [center[0], center[1], radius]