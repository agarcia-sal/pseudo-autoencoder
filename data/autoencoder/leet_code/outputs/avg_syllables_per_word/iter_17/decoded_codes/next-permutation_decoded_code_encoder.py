class Solution:
    def nextPermutation(self, list_of_numbers):
        index_i = len(list_of_numbers) - 2
        while index_i >= 0 and list_of_numbers[index_i] >= list_of_numbers[index_i + 1]:
            index_i -= 1

        if index_i >= 0:
            index_j = len(list_of_numbers) - 1
            while list_of_numbers[index_j] <= list_of_numbers[index_i]:
                index_j -= 1
            self.SwapElements(list_of_numbers, index_i, index_j)

        self.ReverseSequenceFromPosition(list_of_numbers, index_i + 1)

    def SwapElements(self, list_of_numbers, position_a, position_b):
        list_of_numbers[position_a], list_of_numbers[position_b] = list_of_numbers[position_b], list_of_numbers[position_a]

    def ReverseSequenceFromPosition(self, list_of_numbers, start_position):
        left_pointer = start_position
        right_pointer = len(list_of_numbers) - 1
        while left_pointer < right_pointer:
            self.SwapElements(list_of_numbers, left_pointer, right_pointer)
            left_pointer += 1
            right_pointer -= 1