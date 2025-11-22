from bisect import bisect_left
from typing import List

class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        # Pair each interval's start time with its index, then sort by start time
        start_times = sorted((interval[0], idx) for idx, interval in enumerate(intervals))
        result = []
        for _, end in intervals:
            idx = bisect_left(start_times, (end,))
            if idx < len(start_times):
                result.append(start_times[idx][1])
            else:
                result.append(-1)
        return result