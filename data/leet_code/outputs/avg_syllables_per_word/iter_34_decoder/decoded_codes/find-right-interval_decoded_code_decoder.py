from bisect import bisect_left
from typing import List

class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        start_times = [(interval[0], i) for i, interval in enumerate(intervals)]
        start_times.sort(key=lambda x: x[0])

        result = []
        starts = [st[0] for st in start_times]  # for binary search

        for interval in intervals:
            end_value = interval[1]
            search_index = bisect_left(starts, end_value)
            if search_index < len(start_times):
                result.append(start_times[search_index][1])
            else:
                result.append(-1)
        return result