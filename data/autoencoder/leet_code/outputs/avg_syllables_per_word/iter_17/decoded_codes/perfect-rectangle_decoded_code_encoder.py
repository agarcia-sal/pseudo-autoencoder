class Solution:
    def isRectangleCover(self, list_of_rectangles):
        X1 = float('inf')
        Y1 = float('inf')
        X2 = float('-inf')
        Y2 = float('-inf')

        points = set()
        total_area = 0

        for rectangle in list_of_rectangles:
            x1, y1, x2, y2 = rectangle

            X1 = min(X1, x1)
            Y1 = min(Y1, y1)
            X2 = max(X2, x2)
            Y2 = max(Y2, y2)

            rectangle_area = (x2 - x1) * (y2 - y1)
            total_area += rectangle_area

            corner_points = [(x1, y1), (x1, y2), (x2, y1), (x2, y2)]

            for point in corner_points:
                if point in points:
                    points.remove(point)
                else:
                    points.add(point)

        if total_area != (X2 - X1) * (Y2 - Y1):
            return False

        expected_points = {(X1, Y1), (X1, Y2), (X2, Y1), (X2, Y2)}

        if points != expected_points:
            return False

        return True