from typing import List
import bisect

class Solution:
    def minOperations(self, target: List[int], arr: List[int]) -> int:
        index_map = {value: index for index, value in enumerate(target)}
        transformed_arr = [index_map[value] for value in arr if value in index_map]

        lis = []
        for num in transformed_arr:
            pos = bisect.bisect_left(lis, num)
            if pos == len(lis):
                lis.append(num)
            else:
                lis[pos] = num

        lcs_length = len(lis)
        return len(target) - lcs_length