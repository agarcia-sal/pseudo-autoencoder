from typing import List

class Solution:
    def search(self, list_of_numbers: List[int], target_value: int) -> int:
        left, right = 0, len(list_of_numbers) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if list_of_numbers[mid] == target_value:
                return mid
            if list_of_numbers[left] <= list_of_numbers[mid]:
                if list_of_numbers[left] <= target_value < list_of_numbers[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                if list_of_numbers[mid] < target_value <= list_of_numbers[right]:
                    left = mid + 1
                else:
                    right = mid - 1
        return -1