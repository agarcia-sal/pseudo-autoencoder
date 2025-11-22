class Solution:
    def wiggleSort(self, list_of_numbers):
        list_of_numbers.sort()
        sorted_numbers = list_of_numbers[:]
        length_of_numbers = len(list_of_numbers)
        left_pointer = (length_of_numbers - 1) // 2
        right_pointer = length_of_numbers - 1
        for index in range(length_of_numbers):
            if index % 2 == 0:
                list_of_numbers[index] = sorted_numbers[left_pointer]
                left_pointer -= 1
            else:
                list_of_numbers[index] = sorted_numbers[right_pointer]
                right_pointer -= 1