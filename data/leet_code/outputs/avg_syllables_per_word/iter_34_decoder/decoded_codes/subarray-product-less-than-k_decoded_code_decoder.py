class Solution:
    def numSubarrayProductLessThanK(self, nums, k) -> int:
        if k <= 1:
            return 0
        product = 1
        left = 0
        count = 0
        for right in range(len(nums)):
            product *= nums[right]
            while product >= k and left <= right:
                product //= nums[left] if isinstance(product, int) else nums[left]
                # Using float division to handle non-integer products properly
                if product == 0:
                    product = 1  # reset product if zero occurs to avoid infinite loop
                left += 1
            count += right - left + 1
        return count