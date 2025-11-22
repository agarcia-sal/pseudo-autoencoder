from bisect import bisect_left
from typing import List

class Solution:
    def minOperations(self, target: List[int], arr: List[int]) -> int:
        index_map = {value: idx for idx, value in enumerate(target)}

        transformed_arr = [index_map[v] for v in arr if v in index_map]

        lis = []
        for number in transformed_arr:
            pos = bisect_left(lis, number)
            if pos == len(lis):
                lis.append(number)
            else:
                lis[pos] = number

        lcs_length = len(lis)
        minimum_operations = len(target) - lcs_length
        return minimum_operations