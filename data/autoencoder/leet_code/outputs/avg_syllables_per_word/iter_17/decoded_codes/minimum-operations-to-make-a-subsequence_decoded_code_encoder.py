class Solution:
    def minOperations(self, target_list, arr_list):
        index_map = self.createIndexMap(target_list)
        transformed_arr = self.transformArray(arr_list, index_map)
        lis = self.findLongestIncreasingSubsequence(transformed_arr)
        lcs_length = len(lis)
        return len(target_list) - lcs_length

    def createIndexMap(self, list_of_values):
        mapping = dict()
        index_counter = 0
        for value in list_of_values:
            mapping[value] = index_counter
            index_counter += 1
        return mapping

    def transformArray(self, array, mapping):
        transformed_list = []
        for value in array:
            if value in mapping:
                transformed_list.append(mapping[value])
        return transformed_list

    def findLongestIncreasingSubsequence(self, sequence):
        lis = []
        for number in sequence:
            position = self.findInsertPosition(lis, number)
            if position == len(lis):
                lis.append(number)
            else:
                lis[position] = number
        return lis

    def findInsertPosition(self, sorted_list, target_value):
        left, right = 0, len(sorted_list) - 1
        while left <= right:
            mid = (left + right) // 2
            if sorted_list[mid] < target_value:
                left = mid + 1
            else:
                right = mid - 1
        return left