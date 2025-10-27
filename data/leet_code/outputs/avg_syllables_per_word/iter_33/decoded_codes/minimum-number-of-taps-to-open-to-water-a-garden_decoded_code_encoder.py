from typing import List

class Solution:
    def minTaps(self, n: int, ranges: List[int]) -> int:
        max_range = [0] * (n + 1)
        for i in range(n + 1):
            if ranges[i] > 0:
                left = max(0, i - ranges[i])
                right = min(n, i + ranges[i])
                if max_range[left] < right:
                    max_range[left] = right

        taps = 0
        current_end = 0
        farthest = 0
        for i in range(n + 1):
            if i > farthest:
                return -1
            if i > current_end:
                taps += 1
                current_end = farthest
            if farthest < max_range[i]:
                farthest = max_range[i]

        return taps