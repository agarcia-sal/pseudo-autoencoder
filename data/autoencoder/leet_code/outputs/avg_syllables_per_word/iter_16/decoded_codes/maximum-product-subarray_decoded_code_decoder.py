class Solution:
    def maxProduct(self, nums):
        if len(nums) == 0:
            return 0
        max_product = nums[0]
        min_product = nums[0]
        result = nums[0]
        for num in nums[1:]:
            if num < 0:
                max_product, min_product = min_product, max_product
            if num > max_product * num:
                max_product = num
            else:
                max_product = max_product * num
            if num < min_product * num:
                min_product = num
            else:
                min_product = min_product * num
            if result < max_product:
                result = max_product
        return result