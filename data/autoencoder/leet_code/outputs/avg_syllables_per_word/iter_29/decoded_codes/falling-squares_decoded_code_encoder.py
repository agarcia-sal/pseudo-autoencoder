from typing import List, Tuple

class Solution:
    def fallingSquares(self, positions: List[Tuple[int, int]]) -> List[int]:
        max_heights = []
        intervals = []
        current_max_height = 0

        for position in positions:
            left, side_length = position
            right = left + side_length - 1
            height = side_length

            for interval_left, interval_right, interval_height in intervals:
                if left <= interval_right and right >= interval_left:
                    height = max(height, side_length + interval_height)

            intervals.append((left, right, height))
            current_max_height = max(current_max_height, height)
            max_heights.append(current_max_height)

        return max_heights