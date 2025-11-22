from bisect import bisect_left
from typing import List

class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        list_of_start_and_index_pairs = sorted((interval[0], idx) for idx, interval in enumerate(intervals))
        result_list = []
        for _, end in intervals:
            search_index = bisect_left(list_of_start_and_index_pairs, (end,))
            if search_index < len(list_of_start_and_index_pairs):
                result_list.append(list_of_start_and_index_pairs[search_index][1])
            else:
                result_list.append(-1)
        return result_list