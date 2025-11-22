from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length_of_nums = len(nums)
        answer = [1] * length_of_nums

        left_product = 1
        for index in range(length_of_nums):
            answer[index] = left_product
            left_product *= nums[index]

        right_product = 1
        for index in range(length_of_nums - 1, -1, -1):
            answer[index] *= right_product
            right_product *= nums[index]

        return answer