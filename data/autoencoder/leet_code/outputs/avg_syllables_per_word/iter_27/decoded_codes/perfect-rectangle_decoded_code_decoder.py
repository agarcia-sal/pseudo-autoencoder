from typing import List, Tuple, Set

class Solution:
    def isRectangleCover(self, rectangles: List[List[int]]) -> bool:
        X1 = float('inf')
        Y1 = float('inf')
        X2 = float('-inf')
        Y2 = float('-inf')

        points: Set[Tuple[int, int]] = set()
        area = 0

        for rectangle in rectangles:
            x1, y1, x2, y2 = rectangle

            if x1 >= x2 or y1 >= y2:
                # Invalid rectangle with zero or negative area
                return False

            X1 = min(X1, x1)
            Y1 = min(Y1, y1)
            X2 = max(X2, x2)
            Y2 = max(Y2, y2)

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