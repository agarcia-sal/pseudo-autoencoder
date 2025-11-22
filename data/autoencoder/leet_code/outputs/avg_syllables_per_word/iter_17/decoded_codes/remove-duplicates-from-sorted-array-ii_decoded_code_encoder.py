class Solution:
    def removeDuplicates(self, list_of_numbers):
        if not list_of_numbers:
            return 0

        write_index = 0

        for index in range(min(2, len(list_of_numbers))):
            list_of_numbers[write_index] = list_of_numbers[index]
            write_index += 1

        for index in range(2, len(list_of_numbers)):
            if list_of_numbers[index] != list_of_numbers[write_index - 2]:
                list_of_numbers[write_index] = list_of_numbers[index]
                write_index += 1

        return write_index