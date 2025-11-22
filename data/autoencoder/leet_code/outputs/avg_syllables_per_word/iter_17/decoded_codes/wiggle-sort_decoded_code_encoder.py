class Solution:
    def wiggleSort(self, list_of_numbers):
        less = True
        for i in range(len(list_of_numbers) - 1):
            if less:
                if list_of_numbers[i] > list_of_numbers[i + 1]:
                    list_of_numbers[i], list_of_numbers[i + 1] = list_of_numbers[i + 1], list_of_numbers[i]
            else:
                if list_of_numbers[i] < list_of_numbers[i + 1]:
                    list_of_numbers[i], list_of_numbers[i + 1] = list_of_numbers[i + 1], list_of_numbers[i]
            less = not less