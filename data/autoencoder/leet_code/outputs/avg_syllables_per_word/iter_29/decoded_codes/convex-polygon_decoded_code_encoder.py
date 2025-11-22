from typing import List

class Solution:
    def isConvex(self, points: List[List[int]]) -> bool:
        def cross_product(origin_point: List[int], a_point: List[int], b_point: List[int]) -> int:
            # Calculate the cross product of vectors OA and OB
            first_difference_x = a_point[0] - origin_point[0]
            second_difference_y = b_point[1] - origin_point[1]
            third_difference_y = a_point[1] - origin_point[1]
            fourth_difference_x = b_point[0] - origin_point[0]
            return first_difference_x * second_difference_y - third_difference_y * fourth_difference_x

        number_of_points = len(points)
        if number_of_points <= 3:
            return True

        orientation = 0

        for index in range(number_of_points):
            origin = points[index]
            point_a = points[(index + 1) % number_of_points]
            point_b = points[(index + 2) % number_of_points]
            cross = cross_product(origin, point_a, point_b)

            if cross != 0:
                if orientation == 0:
                    orientation = 1 if cross > 0 else -1
                elif (orientation == 1 and cross < 0) or (orientation == -1 and cross > 0):
                    return False

        return True