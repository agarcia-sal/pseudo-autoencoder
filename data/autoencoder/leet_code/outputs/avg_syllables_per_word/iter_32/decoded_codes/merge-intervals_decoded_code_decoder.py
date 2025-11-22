from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # Sort intervals by their start time
        intervals.sort(key=lambda x: x[0])

        merged = []
        for interval in intervals:
            # If merged is empty or current interval does not overlap with last merged interval
            if not merged or merged[-1][1] < interval[0]:
                merged.append(interval)
            else:
                # Overlapping intervals, merge by updating the end time
                merged[-1][1] = max(merged[-1][1], interval[1])
        return merged