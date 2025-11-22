from bisect import bisect_left
from typing import List, Tuple

class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        start_times: List[Tuple[int, int]] = sorted((interval[0], i) for i, interval in enumerate(intervals))
        result: List[int] = []
        starts = [start for start, _ in start_times]

        for interval in intervals:
            end = interval[1]
            idx = bisect_left(starts, end)
            if idx < len(start_times):
                result.append(start_times[idx][1])
            else:
                result.append(-1)
        return result