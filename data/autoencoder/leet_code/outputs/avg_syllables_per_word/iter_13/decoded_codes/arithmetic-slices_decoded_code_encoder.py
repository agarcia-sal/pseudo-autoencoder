class Solution:
    def numberOfArithmeticSlices(self, nums):
        if len(nums) < 3:
            return 0

        total_slices = 0
        current_length = 2

        for i in range(2, len(nums)):
            if nums[i] - nums[i - 1] == nums[i - 1] - nums[i - 2]:
                current_length += 1
                total_slices += current_length - 2
            else:
                current_length = 2

        return total_slices