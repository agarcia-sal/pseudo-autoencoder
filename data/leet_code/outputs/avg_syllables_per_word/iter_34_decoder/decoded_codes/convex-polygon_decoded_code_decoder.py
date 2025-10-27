from typing import List

class Solution:
    def isConvex(self, points: List[List[int]]) -> bool:
        def cross_product(o: List[int], a: List[int], b: List[int]) -> int:
            # Cross product of vectors OA and OB
            first_difference_x = a[0] - o[0]
            second_difference_y = b[1] - o[1]
            first_term = first_difference_x * second_difference_y

            first_difference_y = a[1] - o[1]
            second_difference_x = b[0] - o[0]
            second_term = first_difference_y * second_difference_x

            cross_value = first_term - second_term
            return cross_value

        n = len(points)
        if n <= 3:
            return True

        orientation = 0

        for i in range(n):
            o = points[i]
            a = points[(i + 1) % n]
            b = points[(i + 2) % n]

            cross = cross_product(o, a, b)

            if cross != 0:
                if orientation == 0:
                    orientation = 1 if cross > 0 else -1
                elif orientation == 1 and cross < 0:
                    return False
                elif orientation == -1 and cross > 0:
                    return False

        return True