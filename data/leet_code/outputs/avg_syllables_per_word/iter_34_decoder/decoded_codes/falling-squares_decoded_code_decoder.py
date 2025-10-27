from typing import List, Tuple

class Solution:  
    def fallingSquares(self, positions: List[Tuple[int, int]]) -> List[int]:
        max_heights = []
        intervals = []
        current_max_height = 0

        for pos in positions:
            left, side_length = pos
            right = left + side_length - 1
            height = side_length

            for interval in intervals:
                interval_left, interval_right, interval_height = interval
                if left <= interval_right and right >= interval_left:
                    candidate_height = side_length + interval_height
                    if height < candidate_height:
                        height = candidate_height

            intervals.append((left, right, height))
            if current_max_height < height:
                current_max_height = height
            max_heights.append(current_max_height)

        return max_heights