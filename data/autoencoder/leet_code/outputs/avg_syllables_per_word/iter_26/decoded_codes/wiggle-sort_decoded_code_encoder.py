class Solution:
    def wiggleSort(self, list_of_numbers: list[int]) -> None:
        flag_less = True

        for index in range(len(list_of_numbers) - 1):
            if flag_less:
                if list_of_numbers[index] > list_of_numbers[index + 1]:
                    list_of_numbers[index], list_of_numbers[index + 1] = list_of_numbers[index + 1], list_of_numbers[index]
            else:
                if list_of_numbers[index] < list_of_numbers[index + 1]:
                    list_of_numbers[index], list_of_numbers[index + 1] = list_of_numbers[index + 1], list_of_numbers[index]
            flag_less = not flag_less