from bisect import bisect_left
from typing import List

class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        # Create a sorted list of (start_time, original_index) pairs
        start_times = sorted((start, i) for i, (start, _) in enumerate(intervals))
        result = []

        for _, end_time in intervals:
            # Find the smallest start_time >= end_time using binary search
            pos = bisect_left(start_times, (end_time, -1))
            if pos < len(start_times):
                result.append(start_times[pos][1])
            else:
                result.append(-1)

        return result