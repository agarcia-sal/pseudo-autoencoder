class Solution:
    def isRectangleCover(self, rectangles):
        X1 = float('inf')
        Y1 = float('inf')
        X2 = float('-inf')
        Y2 = float('-inf')
        points = set()
        area = 0
        for rect in rectangles:
            x1, y1, x2, y2 = rect
            if x1 < X1:
                X1 = x1
            if y1 < Y1:
                Y1 = y1
            if x2 > X2:
                X2 = x2
            if y2 > Y2:
                Y2 = y2
            current_area = (x2 - x1) * (y2 - y1)
            area += current_area
            for point in [(x1, y1), (x1, y2), (x2, y1), (x2, y2)]:
                if point in points:
                    points.remove(point)
                else:
                    points.add(point)
        expected_area = (X2 - X1) * (Y2 - Y1)
        if area != expected_area:
            return False
        expected_corners = {(X1, Y1), (X1, Y2), (X2, Y1), (X2, Y2)}
        if points != expected_corners:
            return False
        return True