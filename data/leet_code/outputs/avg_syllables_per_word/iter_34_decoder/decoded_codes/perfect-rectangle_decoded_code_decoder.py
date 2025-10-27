class Solution:
    def isRectangleCover(self, rectangles):
        X1, Y1 = float('inf'), float('inf')
        X2, Y2 = float('-inf'), float('-inf')
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

            current_area = (x2 - x1) * (y2 - y1)
            area += current_area

            for p in [(x1, y1), (x1, y2), (x2, y1), (x2, y2)]:
                if p in points:
                    points.remove(p)
                else:
                    points.add(p)

        expected_area = (X2 - X1) * (Y2 - Y1)
        if area != expected_area:
            return False

        expected_points = {(X1, Y1), (X1, Y2), (X2, Y1), (X2, Y2)}
        if points != expected_points:
            return False

        return True