class Solution:
    def maxSubArray(self, nums):
        max_sum = current_sum = nums[0]
        for num in nums[1:]:
            current_sum = num if num > current_sum + num else current_sum + num
            if max_sum < current_sum:
                max_sum = current_sum
        return max_sum