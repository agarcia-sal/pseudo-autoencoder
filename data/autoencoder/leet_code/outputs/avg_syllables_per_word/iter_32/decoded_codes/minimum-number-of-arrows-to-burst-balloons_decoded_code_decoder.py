from typing import List
import math

class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        # Sort balloons based on their end coordinate
        points.sort(key=lambda x: x[1])
        arrows = 0
        last_arrow_position = -math.inf  # negative infinity
        for balloon in points:
            # If the start of the balloon is beyond the last arrow shot position,
            # we need a new arrow
            if balloon[0] > last_arrow_position:
                arrows += 1
                last_arrow_position = balloon[1]
        return arrows