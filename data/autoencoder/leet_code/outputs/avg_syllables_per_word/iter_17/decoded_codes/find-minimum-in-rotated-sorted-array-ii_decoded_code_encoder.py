from typing import List

class Solution:
    def findMin(self, list_of_numbers: List[int]) -> int:
        left, right = 0, len(list_of_numbers) - 1
        while left < right:
            mid = (left + right) // 2
            if list_of_numbers[mid] > list_of_numbers[right]:
                left = mid + 1
            elif list_of_numbers[mid] < list_of_numbers[right]:
                right = mid
            else:
                right -= 1
        return list_of_numbers[left]