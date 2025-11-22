from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        merged_list = []
        for interval in intervals:
            if not merged_list or merged_list[-1][1] < interval[0]:
                merged_list.append(interval)
            else:
                merged_list[-1][1] = max(merged_list[-1][1], interval[1])
        return merged_list