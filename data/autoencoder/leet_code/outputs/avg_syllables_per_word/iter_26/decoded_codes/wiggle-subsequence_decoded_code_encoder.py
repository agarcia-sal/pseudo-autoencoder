class Solution:
    def wiggleMaxLength(self, list_of_numbers):
        if len(list_of_numbers) < 2:
            return len(list_of_numbers)

        upward_count = 1
        downward_count = 1

        for index in range(1, len(list_of_numbers)):
            if list_of_numbers[index] > list_of_numbers[index - 1]:
                upward_count = downward_count + 1
            elif list_of_numbers[index] < list_of_numbers[index - 1]:
                downward_count = upward_count + 1

        return max(upward_count, downward_count)