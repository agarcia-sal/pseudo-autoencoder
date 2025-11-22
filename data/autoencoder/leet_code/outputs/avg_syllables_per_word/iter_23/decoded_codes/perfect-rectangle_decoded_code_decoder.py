from typing import List, Tuple

class Solution:
    def isRectangleCover(self, rectangles: List[List[int]]) -> bool:
        X1 = float('inf')    # min x
        Y1 = float('inf')    # min y
        X2 = float('-inf')   # max x
        Y2 = float('-inf')   # max y
        points = set()
        area = 0

        for rect in rectangles:
            x1, y1, x2, y2 = rect
            if X1 > x1:
                X1 = x1
            if Y1 > y1:
                Y1 = y1
            if X2 < x2:
                X2 = x2
            if Y2 < y2:
                Y2 = y2

            rect_area = (x2 - x1) * (y2 - y1)
            area += rect_area

            # For each corner point, add/remove from the set
            for p in [(x1, y1), (x1, y2), (x2, y1), (x2, y2)]:
                if p in points:
                    points.remove(p)
                else:
                    points.add(p)

        large_rectangle_area = (X2 - X1) * (Y2 - Y1)
        if area != large_rectangle_area:
            return False

        expected_corners = {(X1, Y1), (X1, Y2), (X2, Y1), (X2, Y2)}
        if points != expected_corners:
            return False

        return True