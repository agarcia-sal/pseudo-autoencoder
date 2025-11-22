from typing import List
import math

class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key=lambda balloon: balloon[1])
        arrows = 0
        last_arrow_position = -math.inf
        for balloon in points:
            if balloon[0] > last_arrow_position:
                arrows += 1
                last_arrow_position = balloon[1]
        return arrows