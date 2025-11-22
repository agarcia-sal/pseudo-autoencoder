from typing import List

class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k <= 1:
            return 0
        product_value = 1
        left_pointer = 0
        count_subarrays = 0

        for right_pointer in range(len(nums)):
            product_value *= nums[right_pointer]
            while product_value >= k and left_pointer <= right_pointer:
                product_value //= nums[left_pointer]
                left_pointer += 1
            count_subarrays += right_pointer - left_pointer + 1

        return count_subarrays