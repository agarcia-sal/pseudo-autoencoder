from bisect import bisect_left
from typing import List, Tuple

class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        start_times: List[Tuple[int, int]] = sorted((interval[0], i) for i, interval in enumerate(intervals))
        result: List[int] = []
        for _, end in intervals:
            idx = bisect_left(start_times, (end,))
            if idx < len(start_times):
                result.append(start_times[idx][1])
            else:
                result.append(-1)
        return result