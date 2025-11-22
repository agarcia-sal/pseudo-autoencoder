from typing import List

class Solution:
    def intersectionSizeTwo(self, intervals: List[List[int]]) -> int:
        # Sort by end ascending, and start descending
        intervals.sort(key=lambda x: (x[1], -x[0]))

        first = intervals[0][1] - 1
        second = intervals[0][1]
        count = 2

        for start, end in intervals[1:]:
            if start > second:
                # No overlap with current points, pick two new points
                first = end - 1
                second = end
                count += 2
            elif start > first:
                # Overlaps with one point, pick one new point
                first = second
                second = end
                count += 1
            # else: already covered by first and second, do nothing

        return count