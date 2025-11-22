from bisect import bisect_left
from typing import List

class Solution:
    def minOperations(self, target: List[int], arr: List[int]) -> int:
        index_map = {}
        current_index = 0
        for value in target:
            index_map[value] = current_index
            current_index += 1

        transformed_arr = []
        for value in arr:
            if value in index_map:
                transformed_arr.append(index_map[value])

        lis = []
        for num in transformed_arr:
            position = bisect_left(lis, num)
            if position == len(lis):
                lis.append(num)
            else:
                lis[position] = num

        lcs_length = len(lis)
        return len(target) - lcs_length