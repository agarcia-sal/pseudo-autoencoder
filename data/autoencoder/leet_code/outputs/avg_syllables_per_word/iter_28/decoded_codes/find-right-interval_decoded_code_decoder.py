from bisect import bisect_left
from typing import List

class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        start_with_index = sorted((start, i) for i, (start, _) in enumerate(intervals))
        result = []
        starts = [start for start, _ in start_with_index]
        for _, end in intervals:
            pos = bisect_left(starts, end)
            if pos < len(start_with_index):
                result.append(start_with_index[pos][1])
            else:
                result.append(-1)
        return result