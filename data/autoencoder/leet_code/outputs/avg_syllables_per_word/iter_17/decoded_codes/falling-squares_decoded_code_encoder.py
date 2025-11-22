from typing import List

class Solution:
    def fallingSquares(self, positions: List[List[int]]) -> List[int]:
        max_heights = []
        intervals = []
        current_max_height = 0

        for left_and_side_length in positions:
            left = left_and_side_length[0]
            side_length = left_and_side_length[1]
            right = left + side_length - 1
            height = side_length

            for interval in intervals:
                interval_left, interval_right, interval_height = interval
                # Check if current square overlaps with interval
                if left <= interval_right and right >= interval_left:
                    height = max(height, side_length + interval_height)

            intervals.append((left, right, height))
            current_max_height = max(current_max_height, height)
            max_heights.append(current_max_height)

        return max_heights