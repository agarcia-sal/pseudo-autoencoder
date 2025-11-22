class Solution:
    def findUnsortedSubarray(self, list_of_numbers):
        sorted_list = sorted(list_of_numbers)
        start = -1
        end = -2
        for index in range(len(list_of_numbers)):
            if list_of_numbers[index] != sorted_list[index]:
                if start == -1:
                    start = index
                end = index
        return end - start + 1