import random
import math

class Solution:
    def outerTrees(self, trees):
        def dist_sq(p1, p2):
            difference_x = p1[0] - p2[0]
            difference_y = p1[1] - p2[1]
            square_difference_x = difference_x * difference_x
            square_difference_y = difference_y * difference_y
            sum_of_squares = square_difference_x + square_difference_y
            return sum_of_squares

        def circumcenter(p1, p2, p3):
            ax, ay = p1[0], p1[1]
            bx, by = p2[0], p2[1]
            cx, cy = p3[0], p3[1]
            term1 = ax * (by - cy)
            term2 = bx * (cy - ay)
            term3 = cx * (ay - by)
            d = 2 * (term1 + term2 + term3)

            ax_squared = ax * ax
            ay_squared = ay * ay
            bx_squared = bx * bx
            by_squared = by * by
            cx_squared = cx * cx
            cy_squared = cy * cy

            numerator_ux_part1 = (ax_squared + ay_squared) * (by - cy)
            numerator_ux_part2 = (bx_squared + by_squared) * (cy - ay)
            numerator_ux_part3 = (cx_squared + cy_squared) * (ay - by)
            ux = (numerator_ux_part1 + numerator_ux_part2 + numerator_ux_part3) / d

            numerator_uy_part1 = (ax_squared + ay_squared) * (cx - bx)
            numerator_uy_part2 = (bx_squared + by_squared) * (ax - cx)
            numerator_uy_part3 = (cx_squared + cy_squared) * (bx - ax)
            uy = (numerator_uy_part1 + numerator_uy_part2 + numerator_uy_part3) / d

            center = [ux, uy]
            difference_ux_ax = ux - ax
            difference_uy_ay = uy - ay
            square_difference_ux_ax = difference_ux_ax * difference_ux_ax
            square_difference_uy_ay = difference_uy_ay * difference_uy_ay
            radius = math.sqrt(square_difference_ux_ax + square_difference_uy_ay)
            return center, radius

        def welzl(points, boundary, n):
            if n == 0 or len(boundary) == 3:
                if len(boundary) == 0:
                    return [0, 0], 0
                elif len(boundary) == 1:
                    return boundary[0], 0
                elif len(boundary) == 2:
                    first_x = boundary[0][0]
                    second_x = boundary[1][0]
                    first_y = boundary[0][1]
                    second_y = boundary[1][1]
                    center_x = (first_x + second_x) / 2
                    center_y = (first_y + second_y) / 2
                    center = [center_x, center_y]
                    distance_square = dist_sq(boundary[0], boundary[1])
                    radius = math.sqrt(distance_square) / 2
                    return center, radius
                else:
                    return circumcenter(boundary[0], boundary[1], boundary[2])

            p = points[n - 1]
            result_center, result_radius = welzl(points, boundary, n - 1)
            distance_center_p = dist_sq(result_center, p)
            if distance_center_p <= result_radius * result_radius:
                return result_center, result_radius

            return welzl(points, boundary + [p], n - 1)

        random.shuffle(trees)
        center, radius = welzl(trees, [], len(trees))
        return [center[0], center[1], radius]