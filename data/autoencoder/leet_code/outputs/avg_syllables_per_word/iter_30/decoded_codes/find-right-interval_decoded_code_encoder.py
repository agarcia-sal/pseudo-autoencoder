from bisect import bisect_left
from typing import List

class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        # Create a sorted list of (start, original index) pairs
        start_times = sorted((interval[0], i) for i, interval in enumerate(intervals))
        starts = [start for start, _ in start_times]

        result = []
        for _, end in intervals:
            # Find the index of the smallest start >= end using binary search
            idx = bisect_left(starts, end)
            if idx < len(start_times):
                result.append(start_times[idx][1])
            else:
                result.append(-1)
        return result