from typing import List

class Solution:
    def intersectionSizeTwo(self, intervals: List[List[int]]) -> int:
        # Sort intervals by their end ascending, and if tie by start descending
        intervals.sort(key=lambda x: (x[1], -x[0]))

        # Initialize first and second points with the last two points of the first interval
        first = intervals[0][1] - 1
        second = intervals[0][1]
        count = 2

        for start, end in intervals[1:]:
            if start > second:
                # Need to add two points at the end of this interval
                first = end - 1
                second = end
                count += 2
            elif start > first:
                # Need to add one point
                first = second
                second = end
                count += 1
            # else: start <= first means interval already covered by first and second

        return count