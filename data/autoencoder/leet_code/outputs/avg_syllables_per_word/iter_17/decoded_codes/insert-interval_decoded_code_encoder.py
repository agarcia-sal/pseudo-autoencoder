from typing import List

class Solution:
    def insert(self, list_of_intervals: List[List[int]], new_interval: List[int]) -> List[List[int]]:
        if not list_of_intervals:
            return [new_interval]

        merged_intervals = []
        index = 0
        total_intervals = len(list_of_intervals)

        # Add all intervals ending before new_interval starts
        while index < total_intervals and list_of_intervals[index][1] < new_interval[0]:
            merged_intervals.append(list_of_intervals[index])
            index += 1

        # Merge overlapping intervals with new_interval
        while index < total_intervals and list_of_intervals[index][0] <= new_interval[1]:
            new_interval[0] = min(new_interval[0], list_of_intervals[index][0])
            new_interval[1] = max(new_interval[1], list_of_intervals[index][1])
            index += 1

        # Add the merged new_interval
        merged_intervals.append(new_interval)

        # Add the remaining intervals
        while index < total_intervals:
            merged_intervals.append(list_of_intervals[index])
            index += 1

        return merged_intervals