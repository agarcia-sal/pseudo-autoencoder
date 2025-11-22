from bisect import bisect_left
from typing import List

class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        # Prepare a list of (start_time, original_index) pairs
        start_times = [(interval[0], i) for i, interval in enumerate(intervals)]
        # Sort by start_time in ascending order
        start_times.sort(key=lambda x: x[0])

        result = []
        # Extract sorted start times separately for binary search
        sorted_starts = [st[0] for st in start_times]

        for _, end in intervals:
            # Find the leftmost index where end can be inserted to maintain order
            idx = bisect_left(sorted_starts, end)
            if idx < len(start_times):
                # Append the index of the right interval
                result.append(start_times[idx][1])
            else:
                # No suitable right interval found
                result.append(-1)

        return result