from bisect import bisect_left
from typing import List

class Solution:
    def minOperations(self, target: List[int], arr: List[int]) -> int:
        index_map = {}
        for index, value in enumerate(target):
            index_map[value] = index

        transformed_arr = []
        for value in arr:
            if value in index_map:
                transformed_arr.append(index_map[value])

        lis = []
        for num in transformed_arr:
            pos = bisect_left(lis, num)
            if pos == len(lis):
                lis.append(num)
            else:
                lis[pos] = num

        lcs_length = len(lis)
        result = len(target) - lcs_length
        return result