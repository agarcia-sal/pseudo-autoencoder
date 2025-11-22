class Solution:
    def numSubarrayProductLessThanK(self, nums, k):
        if k <= 1:
            return 0
        product = 1
        left = 0
        count = 0
        for right in range(len(nums)):
            product *= nums[right]
            while product >= k and left <= right:
                product //= nums[left] if product % nums[left] == 0 else nums[left]
                left += 1
            count += right - left + 1
        return count