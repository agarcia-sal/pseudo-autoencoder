from typing import List

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0

        # Sort intervals based on their end time
        intervals.sort(key=lambda x: x[1])

        end = intervals[0][1]
        count = 0

        for i in range(1, len(intervals)):
            # If the start of the current interval is >= end,
            # update end to the current interval's end
            if intervals[i][0] >= end:
                end = intervals[i][1]
            else:
                # Overlapping interval found, increment count
                count += 1

        return count