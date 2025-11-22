from typing import List

class Solution:
    def minTaps(self, n: int, ranges: List[int]) -> int:
        max_range = self.initialize_max_range(n)
        for index in range(n + 1):
            if ranges[index] > 0:
                left = max(0, index - ranges[index])
                right = min(n, index + ranges[index])
                max_range[left] = max(max_range[left], right)
        taps = 0
        current_end = 0
        farthest = 0
        for index in range(n + 1):
            if index > farthest:
                return -1
            if index > current_end:
                taps += 1
                current_end = farthest
            farthest = max(farthest, max_range[index])
        return taps

    def initialize_max_range(self, n: int) -> List[int]:
        return [0] * (n + 1)