from typing import List

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if not intervals or len(intervals) == 0:
            return 0

        # Sort intervals based on their end time
        intervals.sort(key=lambda x: x[1])

        end = intervals[0][1]
        count = 0

        for i in range(1, len(intervals)):
            if intervals[i][0] >= end:
                end = intervals[i][1]
            else:
                count += 1

        return count