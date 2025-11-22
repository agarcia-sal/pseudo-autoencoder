class Solution:
    def findMin(self, list_of_numbers):
        left, right = 0, len(list_of_numbers) - 1
        if list_of_numbers[left] < list_of_numbers[right]:
            return list_of_numbers[left]
        while left < right:
            mid = (left + right) // 2
            if list_of_numbers[mid] > list_of_numbers[right]:
                left = mid + 1
            else:
                right = mid
        return list_of_numbers[left]