from typing import List

class Solution:
    def intersectionSizeTwo(self, intervals: List[List[int]]) -> int:
        # Sort intervals by their end ascending, then by start descending
        intervals.sort(key=lambda x: (x[1], -x[0]))

        first = intervals[0][1] - 1
        second = intervals[0][1]
        count = 2

        for start, end in intervals[1:]:
            if start > second:
                # New two points needed
                first = end - 1
                second = end
                count += 2
            elif start > first:
                # Only one new point needed
                first = second
                second = end
                count += 1
            # else: both points cover this interval, no increment

        return count