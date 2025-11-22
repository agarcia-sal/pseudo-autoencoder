from typing import List

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if not nums:
            return 0

        max_product = nums[0]
        min_product = nums[0]
        result = nums[0]

        for number in nums[1:]:
            if number < 0:
                max_product, min_product = min_product, max_product

            max_product = max(number, max_product * number)
            min_product = min(number, min_product * number)

            result = max(result, max_product)

        return result