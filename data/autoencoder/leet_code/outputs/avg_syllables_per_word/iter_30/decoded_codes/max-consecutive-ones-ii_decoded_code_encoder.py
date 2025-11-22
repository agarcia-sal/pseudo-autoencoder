from typing import List

class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_count = 0
        current_count = 0
        zero_count = 0
        left = 0
        for right in range(len(nums)):
            if nums[right] == 1:
                current_count += 1
            elif zero_count < 1:
                zero_count += 1
                current_count += 1
            else:
                max_count = max(max_count, current_count)
                while zero_count == 1:
                    if nums[left] == 0:
                        zero_count -= 1
                    current_count -= 1
                    left += 1
                current_count += 1
        max_count = max(max_count, current_count)
        return max_count