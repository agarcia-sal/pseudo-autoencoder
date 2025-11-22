class Solution:
    def search(self, list_of_numbers, target_value):
        left, right = 0, len(list_of_numbers) - 1

        while left <= right:
            middle = left + (right - left) // 2

            if list_of_numbers[middle] == target_value:
                return middle

            if list_of_numbers[left] <= list_of_numbers[middle]:
                if list_of_numbers[left] <= target_value < list_of_numbers[middle]:
                    right = middle - 1
                else:
                    left = middle + 1
            else:
                if list_of_numbers[middle] < target_value <= list_of_numbers[right]:
                    left = middle + 1
                else:
                    right = middle - 1

        return -1