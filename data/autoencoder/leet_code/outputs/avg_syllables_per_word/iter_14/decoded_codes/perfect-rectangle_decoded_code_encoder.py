class Solution:
    def isRectangleCover(self, rectangles):
        X1, Y1 = float('inf'), float('inf')
        X2, Y2 = float('-inf'), float('-inf')
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

            width = x2 - x1
            height = y2 - y1
            area += width * height

            corner_points = [(x1, y1), (x1, y2), (x2, y1), (x2, y2)]
            for point in corner_points:
                if point in points:
                    points.remove(point)
                else:
                    points.add(point)

        expected_area_width = X2 - X1
        expected_area_height = Y2 - Y1

        if area != expected_area_width * expected_area_height:
            return False

        expected_corners = {(X1, Y1), (X1, Y2), (X2, Y1), (X2, Y2)}
        if points != expected_corners:
            return False

        return True