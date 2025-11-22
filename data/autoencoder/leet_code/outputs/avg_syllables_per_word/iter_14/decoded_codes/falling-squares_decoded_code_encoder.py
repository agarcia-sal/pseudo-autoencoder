from typing import List

class Solution:
    def fallingSquares(self, positions: List[List[int]]) -> List[int]:
        max_heights = []
        intervals = []
        current_max_height = 0
        for position in positions:
            left = position[0]
            side_length = position[1]
            right = left + side_length - 1
            height = side_length
            for interval in intervals:
                interval_left, interval_right, interval_height = interval
                # Check for overlap
                if left <= interval_right and right >= interval_left:
                    height = max(height, side_length + interval_height)
            intervals.append([left, right, height])
            if current_max_height < height:
                current_max_height = height
            max_heights.append(current_max_height)
        return max_heights