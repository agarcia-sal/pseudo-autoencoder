class Solution:
    def fallingSquares(self, positions):
        max_heights = []
        intervals = []
        current_max_height = 0
        for left, side_length in positions:
            right = left + side_length - 1
            height = side_length
            for interval_left, interval_right, interval_height in intervals:
                if left <= interval_right and right >= interval_left:
                    if height < side_length + interval_height:
                        height = side_length + interval_height
            intervals.append((left, right, height))
            if current_max_height < height:
                current_max_height = height
            max_heights.append(current_max_height)
        return max_heights