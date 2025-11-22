class Solution:
    def minOperations(self, target, arr):
        index_map = self.create_index_map(target)
        transformed_arr = self.transform_array(arr, index_map)
        lis = self.find_longest_increasing_subsequence(transformed_arr)
        lcs_length = len(lis)
        minimum_operations = len(target) - lcs_length
        return minimum_operations

    def create_index_map(self, target):
        map_object = {}
        index = 0
        for value in target:
            map_object[value] = index
            index += 1
        return map_object

    def transform_array(self, arr, index_map):
        result_list = []
        for value in arr:
            if value in index_map:
                result_list.append(index_map[value])
        return result_list

    def find_longest_increasing_subsequence(self, sequence):
        lis = []
        for num in sequence:
            position = self.binary_search_leftmost(lis, num)
            if position == len(lis):
                lis.append(num)
            else:
                lis[position] = num
        return lis

    def binary_search_leftmost(self, list_values, target_value):
        left, right = 0, len(list_values) - 1
        while left <= right:
            mid = (left + right) // 2
            if list_values[mid] < target_value:
                left = mid + 1
            else:
                right = mid - 1
        return left