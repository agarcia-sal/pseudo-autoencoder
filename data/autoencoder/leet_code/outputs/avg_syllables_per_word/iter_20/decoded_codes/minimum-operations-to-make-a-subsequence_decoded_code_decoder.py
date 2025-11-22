from bisect import bisect_left
from typing import List

class Solution:
    def minOperations(self, target: List[int], arr: List[int]) -> int:
        index_map = {v: i for i, v in enumerate(target)}

        transformed_arr = [index_map[v] for v in arr if v in index_map]

        lis = []
        for num in transformed_arr:
            pos = bisect_left(lis, num)
            if pos == len(lis):
                lis.append(num)
            else:
                lis[pos] = num

        lcs_length = len(lis)
        return len(target) - lcs_length