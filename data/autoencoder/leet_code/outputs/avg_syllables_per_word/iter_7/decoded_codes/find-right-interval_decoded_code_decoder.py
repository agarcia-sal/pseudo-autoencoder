from typing import List, Tuple
import bisect

class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        start_times: List[Tuple[int, int]] = sorted((interval[0], i) for i, interval in enumerate(intervals))
        result: List[int] = []
        for interval in intervals:
            idx = bisect.bisect_left(start_times, (interval[1],))
            if idx < len(start_times):
                result.append(start_times[idx][1])
            else:
                result.append(-1)
        return result