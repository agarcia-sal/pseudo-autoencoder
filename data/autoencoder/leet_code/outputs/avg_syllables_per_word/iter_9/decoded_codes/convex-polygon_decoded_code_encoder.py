class Solution:
    def isConvex(self, points):
        def cross_product(o, a, b):
            return (a[0] - o[0]) * (b[1] - o[1]) - (a[1] - o[1]) * (b[0] - o[0])

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
                current_orientation = 1 if cross > 0 else -1
                if orientation == 0:
                    orientation = current_orientation
                elif orientation != current_orientation:
                    return False
        return True