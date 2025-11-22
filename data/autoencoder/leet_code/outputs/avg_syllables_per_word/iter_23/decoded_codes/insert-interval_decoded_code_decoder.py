from typing import List

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if len(intervals) == 0:
            return [newInterval]

        merged = []
        i = 0
        n = len(intervals)

        # Add all intervals that come before newInterval without overlap
        while i < n and intervals[i][1] < newInterval[0]:
            merged.append(intervals[i])
            i += 1

        # Merge overlapping intervals into newInterval
        while i < n and intervals[i][0] <= newInterval[1]:
            newInterval[0] = min(newInterval[0], intervals[i][0])
            newInterval[1] = max(newInterval[1], intervals[i][1])
            i += 1

        # Add the merged newInterval
        merged.append(newInterval)

        # Add all remaining intervals after newInterval
        while i < n:
            merged.append(intervals[i])
            i += 1

        return merged