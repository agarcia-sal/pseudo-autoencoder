class Solution:
    def findPeakElement(self, list_of_numbers):
        left, right = 0, len(list_of_numbers) - 1
        while left < right:
            mid = (left + right) // 2
            if list_of_numbers[mid] > list_of_numbers[mid + 1]:
                right = mid
            else:
                left = mid + 1
        return left