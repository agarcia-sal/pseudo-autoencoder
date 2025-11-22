class Solution:
    def maxSubArray(self, nums):
        max_sum = nums[0]
        current_sum = nums[0]
        for num in nums[1:]:
            sum_if_added = current_sum + num
            if sum_if_added > num:
                current_sum = sum_if_added
            else:
                current_sum = num
            if current_sum > max_sum:
                max_sum = current_sum
        return max_sum