class Solution:
    def findDuplicates(self, list_of_numbers):
        for i in range(len(list_of_numbers)):
            while list_of_numbers[i] != list_of_numbers[list_of_numbers[i] - 1]:
                first = list_of_numbers[i]
                second = list_of_numbers[first - 1]
                list_of_numbers[first - 1] = first
                list_of_numbers[i] = second
        result_list = []
        for idx, val in enumerate(list_of_numbers):
            if val != idx + 1:
                result_list.append(val)
        return result_list