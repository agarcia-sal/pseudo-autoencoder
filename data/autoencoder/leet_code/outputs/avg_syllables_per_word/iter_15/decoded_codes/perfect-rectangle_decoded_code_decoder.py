from math import inf
from typing import List

class Solution:
    def isRectangleCover(self, rectangles: List[List[int]]) -> bool:
        X1 = inf
        Y1 = inf
        X2 = -inf
        Y2 = -inf

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

            for p in [(x1, y1), (x1, y2), (x2, y1), (x2, y2)]:
                if p in points:
                    points.remove(p)
                else:
                    points.add(p)

        if area != (X2 - X1) * (Y2 - Y1):
            return False

        if points != {(X1, Y1), (X1, Y2), (X2, Y1), (X2, Y2)}:
            return False

        return True