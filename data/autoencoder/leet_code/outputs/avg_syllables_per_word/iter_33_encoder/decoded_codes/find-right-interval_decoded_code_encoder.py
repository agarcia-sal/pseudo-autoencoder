from bisect import bisect_left
from typing import List

class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        start_times = sorted((interval[0], i) for i, interval in enumerate(intervals))
        result = []
        for interval in intervals:
            end_time = interval[1]
            idx = bisect_left(start_times, (end_time,))
            if idx < len(start_times):
                result.append(start_times[idx][1])
            else:
                result.append(-1)
        return result