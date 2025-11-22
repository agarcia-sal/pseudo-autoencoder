from math import inf
from typing import List

class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key=lambda x: x[1])
        number_of_arrows = 0
        last_arrow_position = -inf
        for balloon in points:
            if balloon[0] > last_arrow_position:
                number_of_arrows += 1
                last_arrow_position = balloon[1]
        return number_of_arrows