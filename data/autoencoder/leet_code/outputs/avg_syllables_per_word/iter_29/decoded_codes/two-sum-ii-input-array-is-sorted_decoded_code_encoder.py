from typing import List

class Solution:
    def twoSum(self, numbers_list: List[int], target_value: int) -> List[int]:
        left, right = 0, len(numbers_list) - 1
        while left < right:
            current_sum = numbers_list[left] + numbers_list[right]
            if current_sum == target_value:
                return [left + 1, right + 1]
            elif current_sum < target_value:
                left += 1
            else:
                right -= 1