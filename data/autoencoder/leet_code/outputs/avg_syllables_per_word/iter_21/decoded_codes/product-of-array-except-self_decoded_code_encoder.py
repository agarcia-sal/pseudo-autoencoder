from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        answer = [1] * n

        left_product = 1
        for index in range(n):
            answer[index] = left_product
            left_product *= nums[index]

        right_product = 1
        for index in range(n - 1, -1, -1):
            answer[index] *= right_product
            right_product *= nums[index]

        return answer