from typing import List

class Solution:
    def minTaps(self, n: int, ranges: List[int]) -> int:
        max_range = [0] * (n+1)

        for i in range(n+1):
            if ranges[i] > 0:
                left_bound = max(0, i - ranges[i])
                right_bound = min(n, i + ranges[i])
                max_range[left_bound] = max(max_range[left_bound], right_bound)

        taps = 0
        current_end = 0
        farthest = 0

        for i in range(n+1):
            if i > farthest:
                return -1
            if i > current_end:
                taps += 1
                current_end = farthest
            farthest = max(farthest, max_range[i])

        return taps