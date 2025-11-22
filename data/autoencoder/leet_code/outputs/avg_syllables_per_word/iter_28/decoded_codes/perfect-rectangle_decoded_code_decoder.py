from typing import List

class Solution:
    def isRectangleCover(self, rectangles: List[List[int]]) -> bool:
        bottom_left_x = float('inf')
        bottom_left_y = float('inf')
        top_right_x = float('-inf')
        top_right_y = float('-inf')

        points = set()
        total_area = 0

        for x1, y1, x2, y2 in rectangles:
            if bottom_left_x > x1:
                bottom_left_x = x1
            if bottom_left_y > y1:
                bottom_left_y = y1
            if top_right_x < x2:
                top_right_x = x2
            if top_right_y < y2:
                top_right_y = y2

            total_area += (x2 - x1) * (y2 - y1)

            for point in ((x1, y1), (x1, y2), (x2, y1), (x2, y2)):
                if point in points:
                    points.remove(point)
                else:
                    points.add(point)

        if total_area != (top_right_x - bottom_left_x) * (top_right_y - bottom_left_y):
            return False

        expected_points = {
            (bottom_left_x, bottom_left_y),
            (bottom_left_x, top_right_y),
            (top_right_x, bottom_left_y),
            (top_right_x, top_right_y),
        }
        if points != expected_points:
            return False

        return True