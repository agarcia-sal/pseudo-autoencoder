from typing import List

class Solution:
    def minOperations(self, target: List[int], arr: List[int]) -> int:
        index_map = {}
        index = 0
        for value in target:
            index_map[value] = index
            index += 1

        transformed_arr = []
        for value in arr:
            if value in index_map:
                transformed_arr.append(index_map[value])

        lis = []
        for num in transformed_arr:
            low, high = 0, len(lis) - 1
            while low <= high:
                mid = (low + high) // 2
                if lis[mid] >= num:
                    high = mid - 1
                else:
                    low = mid + 1
            pos = low
            if pos == len(lis):
                lis.append(num)
            else:
                lis[pos] = num

        lcs_length = len(lis)
        return len(target) - lcs_length