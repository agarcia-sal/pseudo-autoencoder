from typing import List, Tuple

class Solution:
    def isConvex(self, points: List[Tuple[int, int]]) -> bool:
        def cross_product(o: Tuple[int, int], a: Tuple[int, int], b: Tuple[int, int]) -> int:
            term_one = a[0] - o[0]
            term_two = b[1] - o[1]
            first_product = term_one * term_two
            term_three = a[1] - o[1]
            term_four = b[0] - o[0]
            second_product = term_three * term_four
            result = first_product - second_product
            return result

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