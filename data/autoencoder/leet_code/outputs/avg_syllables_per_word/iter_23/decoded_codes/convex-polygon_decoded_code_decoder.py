from typing import List

class Solution:
    def isConvex(self, points: List[List[int]]) -> bool:
        def cross_product(o: List[int], a: List[int], b: List[int]) -> int:
            difference_a_zero = a[0] - o[0]
            difference_b_one = b[1] - o[1]
            term_one = difference_a_zero * difference_b_one

            difference_a_one = a[1] - o[1]
            difference_b_zero = b[0] - o[0]
            term_two = difference_a_one * difference_b_zero

            return term_one - term_two

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
                elif (orientation == 1 and cross < 0) or (orientation == -1 and cross > 0):
                    return False

        return True