from typing import List

class Solution:
    def threeSumSmaller(self, nums: List[int], target: int) -> int:
        nums.sort()
        count = 0
        n = len(nums)
        for i in range(n - 2):
            left_pointer, right_pointer = i + 1, n - 1
            while left_pointer < right_pointer:
                current_sum = nums[i] + nums[left_pointer] + nums[right_pointer]
                if current_sum < target:
                    count += right_pointer - left_pointer
                    left_pointer += 1
                else:
                    right_pointer -= 1
        return count