from bisect import bisect_left
from typing import List, Dict

class Solution:
    def minOperations(self, target: List[int], arr: List[int]) -> int:
        index_map = self.build_index_map(target)
        transformed_arr = self.transform_array(arr, index_map)
        lis = self.find_longest_increasing_subsequence(transformed_arr)
        lcs_length = len(lis)
        return len(target) - lcs_length

    def build_index_map(self, target: List[int]) -> Dict[int, int]:
        map_result = {}
        for index in range(len(target)):
            map_result[target[index]] = index
        return map_result

    def transform_array(self, arr: List[int], index_map: Dict[int, int]) -> List[int]:
        result_list = []
        for value in arr:
            if value in index_map:
                result_list.append(index_map[value])
        return result_list

    def find_longest_increasing_subsequence(self, numbers: List[int]) -> List[int]:
        lis = []
        for number in numbers:
            pos = bisect_left(lis, number)
            if pos == len(lis):
                lis.append(number)
            else:
                lis[pos] = number
        return lis