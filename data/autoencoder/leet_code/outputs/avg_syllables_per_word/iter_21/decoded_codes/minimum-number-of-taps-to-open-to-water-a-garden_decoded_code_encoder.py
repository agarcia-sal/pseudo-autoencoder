from typing import List

class Solution:
    def minTaps(self, n: int, ranges: List[int]) -> int:
        max_range = self.initialize_max_range_array(n)

        for position in range(n + 1):
            if ranges[position] > 0:
                left = self.compute_left_boundary(position, ranges[position])
                right = self.compute_right_boundary(n, position, ranges[position])
                max_range[left] = max(max_range[left], right)

        taps = 0
        current_end = 0
        farthest = 0

        for position in range(n + 1):
            if position > farthest:
                return -1
            if position > current_end:
                taps += 1
                current_end = farthest
            farthest = max(farthest, max_range[position])

        return taps

    def initialize_max_range_array(self, n: int) -> List[int]:
        return [0] * (n + 1)

    def compute_left_boundary(self, position: int, range_value: int) -> int:
        return 0 if position - range_value < 0 else position - range_value

    def compute_right_boundary(self, n: int, position: int, range_value: int) -> int:
        return n if position + range_value > n else position + range_value