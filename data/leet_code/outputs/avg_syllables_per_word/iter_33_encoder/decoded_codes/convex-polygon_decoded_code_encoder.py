class Solution:
    def isConvex(self, points):
        def cross_product(o, a, b):
            dx1 = a[0] - o[0]
            dy1 = a[1] - o[1]
            dx2 = b[0] - o[0]
            dy2 = b[1] - o[1]
            return dx1 * dy2 - dy1 * dx2

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