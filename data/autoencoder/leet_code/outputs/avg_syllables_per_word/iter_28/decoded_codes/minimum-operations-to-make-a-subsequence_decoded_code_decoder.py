from bisect import bisect_left
from typing import List

class Solution:
    def minOperations(self, target: List[int], arr: List[int]) -> int:
        index_map = {value: i for i, value in enumerate(target)}
        transformed_arr = [index_map[value] for value in arr if value in index_map]

        lis = []
        for num in transformed_arr:
            pos = bisect_left(lis, num)
            if pos == len(lis):
                lis.append(num)
            else:
                lis[pos] = num

        return len(target) - len(lis)