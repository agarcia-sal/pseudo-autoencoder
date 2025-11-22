from typing import List

class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        self.sort_points_by_end_coordinate(points)
        arrows = 0
        last_arrow_position = float('-inf')
        for balloon in points:
            if balloon[0] > last_arrow_position:
                arrows += 1
                last_arrow_position = balloon[1]
        return arrows

    def sort_points_by_end_coordinate(self, points: List[List[int]]) -> None:
        points.sort(key=lambda x: x[1])