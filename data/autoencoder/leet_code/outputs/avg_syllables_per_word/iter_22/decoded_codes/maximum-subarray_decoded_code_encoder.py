class Solution:
    def maxSubArray(self, nums):
        max_sum = nums[0]
        current_sum = nums[0]
        for num in nums[1:]:
            if num > current_sum + num:
                current_sum = num
            else:
                current_sum = current_sum + num
            if max_sum < current_sum:
                max_sum = current_sum
        return max_sum