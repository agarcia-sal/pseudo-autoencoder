class Solution:
    def isRectangleCover(self, rectangles):
        X1, Y1 = float('inf'), float('inf')
        X2, Y2 = float('-inf'), float('-inf')

        points = set()
        area = 0

        for x1, y1, x2, y2 in rectangles:
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