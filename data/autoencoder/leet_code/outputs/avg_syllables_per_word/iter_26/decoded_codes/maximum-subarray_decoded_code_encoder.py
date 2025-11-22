class Solution:
    def maxSubArray(self, nums):
        maximum_sum = nums[0]
        current_sum = nums[0]
        for number in nums[1:]:
            if number > current_sum + number:
                current_sum = number
            else:
                current_sum = current_sum + number
            if current_sum > maximum_sum:
                maximum_sum = current_sum
        return maximum_sum