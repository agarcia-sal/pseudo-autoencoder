from typing import List, Tuple

class Solution:
    def isConvex(self, points: List[List[int]]) -> bool:
        def cross_product(origin_point: List[int], point_a: List[int], point_b: List[int]) -> int:
            # Compute the z-component of the cross product of vectors OA and OB
            return ((point_a[0] - origin_point[0]) * (point_b[1] - origin_point[1]) -
                    (point_a[1] - origin_point[1]) * (point_b[0] - origin_point[0]))

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