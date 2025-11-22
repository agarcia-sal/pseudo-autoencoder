from typing import List
import bisect

class Solution:
    def minOperations(self, target: List[int], arr: List[int]) -> int:
        index_map = {}
        for index in range(len(target)):
            index_map[target[index]] = index

        transformed_arr = []
        for value in arr:
            if value in index_map:
                transformed_arr.append(index_map[value])

        lis = []
        for num in transformed_arr:
            pos = bisect.bisect_left(lis, num)
            if pos == len(lis):
                lis.append(num)
            else:
                lis[pos] = num

        lcs_length = len(lis)
        return len(target) - lcs_length