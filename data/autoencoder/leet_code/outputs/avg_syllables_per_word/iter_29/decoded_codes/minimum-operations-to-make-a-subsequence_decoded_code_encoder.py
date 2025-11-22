from bisect import bisect_left
from typing import List

class Solution:
    def minOperations(self, target: List[int], arr: List[int]) -> int:
        index_map = {value: idx for idx, value in enumerate(target)}

        transformed_arr = [index_map[val] for val in arr if val in index_map]

        lis = []
        for num in transformed_arr:
            pos = bisect_left(lis, num)
            if pos == len(lis):
                lis.append(num)
            else:
                lis[pos] = num

        lcs_length = len(lis)
        minimum_operations = len(target) - lcs_length
        return minimum_operations