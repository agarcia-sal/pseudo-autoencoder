class Solution:
    def fallingSquares(self, positions):
        intervals = []
        max_heights = []
        current_max_height = 0

        for left, side in positions:
            right = left + side - 1
            height = side
            for il, ir, ih in intervals:
                if left <= ir and right >= il:
                    height = max(height, side + ih)
            intervals.append((left, right, height))
            current_max_height = max(current_max_height, height)
            max_heights.append(current_max_height)

        return max_heights