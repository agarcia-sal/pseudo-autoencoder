class Solution:
    def singleNonDuplicate(self, list_of_numbers):
        left = 0
        right = len(list_of_numbers) - 1
        while left < right:
            mid = left + (right - left) // 2
            if mid % 2 == 1:
                mid -= 1
            if list_of_numbers[mid] == list_of_numbers[mid + 1]:
                left = mid + 2
            else:
                right = mid
        return list_of_numbers[left]