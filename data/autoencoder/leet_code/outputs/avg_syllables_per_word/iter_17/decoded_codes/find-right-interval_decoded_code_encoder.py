from bisect import bisect_left
from typing import List, Tuple

class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        start_times = self.create_sorted_start_times(intervals)
        result = self.create_empty_list()
        for interval in intervals:
            end_position = interval[1]
            idx = self.find_leftmost_index(start_times, end_position)
            if idx < len(start_times):
                result.append(start_times[idx][1])
            else:
                result.append(-1)
        return result

    def create_sorted_start_times(self, intervals: List[List[int]]) -> List[Tuple[int, int]]:
        # Create a list of (start_time, index) tuples, sorted by start_time
        return sorted((start, i) for i, (start, _) in enumerate(intervals))

    def create_empty_list(self) -> List[int]:
        # Return an empty list
        return []

    def find_leftmost_index(self, sorted_list: List[Tuple[int, int]], target_value: int) -> int:
        # Find leftmost position to insert target_value in sorted_list
        # sorted_list is a list of tuples with start times in first position
        leftmost_index = bisect_left(sorted_list, (target_value, -1))
        return leftmost_index