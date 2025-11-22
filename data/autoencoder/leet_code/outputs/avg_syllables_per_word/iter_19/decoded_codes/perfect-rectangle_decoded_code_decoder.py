from math import inf

class Solution:
    def isRectangleCover(self, rectangles):
        X1, Y1 = inf, inf
        X2, Y2 = -inf, -inf
        points = set()
        area = 0

        for x1, y1, x2, y2 in rectangles:
            if X1 > x1:
                X1 = x1
            if Y1 > y1:
                Y1 = y1
            if X2 < x2:
                X2 = x2
            if Y2 < y2:
                Y2 = y2

            area += (x2 - x1) * (y2 - y1)

            corners = [(x1, y1), (x1, y2), (x2, y1), (x2, y2)]
            for p in corners:
                if p in points:
                    points.remove(p)
                else:
                    points.add(p)

        if area != (X2 - X1) * (Y2 - Y1):
            return False

        required_corners = {(X1, Y1), (X1, Y2), (X2, Y1), (X2, Y2)}
        if points != required_corners:
            return False

        return True